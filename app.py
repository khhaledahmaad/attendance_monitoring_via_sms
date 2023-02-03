# Import libraries
import os
import re
import pathlib
import secrets
import pandas as pd
from typing import Dict, Optional
from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from bs4 import BeautifulSoup
import altair as alt
from flask_mail import Mail, Message
from dotenv import load_dotenv
from datetime import date, datetime
from twilio.rest import Client

# Set paths
base_dir = pathlib.Path().absolute()
# Path to all data directories
data = pathlib.Path(base_dir/'datasets')
# Path to credentials data
credentials = data/'credentials'
# Path to raw data
raw = data/'raw'
# Path to processed data
processed = data/'processed'
# Path to environment variables
env_vars = pathlib.Path(base_dir/'env_vars')

# Load dotenv file
load_dotenv(env_vars/'.env.txt')

# Flask app
app = Flask(__name__)
# Configure a secret-key for the flask app
app.config["SECRET_KEY"] = secrets.token_hex(24)

# Configure flask mail app
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Create login_manager app
login_manager = LoginManager(app)
# Create mail app
mail = Mail(app)

# Create twilio client object
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Define a User class to store all the users from the .csv input files
users: Dict[str, "User"] = {}

class User(UserMixin):
    def __init__(self, id: str, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        return users.get(user_id)

    def __str__(self) -> str:
        return f"<Id: {self.id}, Username: {self.username}, Email: {self.email}>"

    def __repr__(self) -> str:
        return self.__str__()

data = pd.read_csv(credentials/'login_credentials.csv')
for index in data.index:
    users[str(index)] = User(
        id=index,
        username=data.loc[index, "first_name"],
        email=data.loc[index, "email"],
        password=data.loc[index, "password"],
    )

# Login endpoint
@login_manager.user_loader
def load_user(user_id: str) -> Optional[User]:
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    # Load data
    df_logins = pd.read_csv(credentials/'login_credentials.csv')
    if request.method == 'POST':
        if request.is_json:
            email = str(request.json['email'])
            password = str(request.json['password'])
        else:
            email = str(request.form['email'])
            password = str(request.form['password'])
            if email=='':
                error='Email Required!'
                return render_template('login.html', error=error)
            elif password=='':
                error='Password Required!'
                return render_template('login.html', error=error)
        if df_logins.loc[df_logins.email==email, 'password'].empty:
            test = False
        else:
            test = (df_logins.email.isin([email]).any()) and (df_logins.loc[df_logins.email==email, 'password'].astype(str).values[0]==password)

        if test: 
            user_id = df_logins.loc[df_logins.email==email].index[0]
            user = User.get(str(user_id))
            login_user(user)
            
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again. If you do not have an account, please create an account first then try logging in.'
    return render_template('login.html', error=error)

# Endpoint for logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Register endpoint
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    # Load Data
    df_logins = pd.read_csv(credentials/'login_credentials.csv')
    df_admins = pd.read_csv(credentials/'admins.csv')
    if request.method == 'POST':
        email = str(request.form['email'])
        test = df_logins.email.isin([email]).any()
        if test:
            message = 'This email already exists. Please click \'Forgotten Password\'.'
            return render_template('register.html', message=message)
        elif request.form['first_name'] == '':
            message = 'First Name is required!'
            return render_template('register.html', message=message)
        elif request.form['last_name'] == '':
            message = 'Last Name is required!'
            return render_template('register.html', message=message)
        elif request.form['email'] == '':
            message = 'Email is required!'
            return render_template('register.html', message=message)
        elif request.form['password'] == '':
            message = 'Password is required!'
            return render_template('register.html', message=message)
        elif request.form['password'] != request.form['confirm_password']:
            message = 'Password should match!'
            return render_template('register.html', message=message)
        elif df_admins.email.isin([str(request.form['email'])]).any()==False:
            message = 'Email not allowed! Please make sure the email entered is in the admin list or contact the administrator!'
            return render_template('register.html', message=message)
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            password = request.form['password']
            
            df = df_logins.append({'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password}, ignore_index=True)
            df.to_csv(credentials/'login_credentials.csv', index=False)
            message = "User created successfully. Please go back to log in."
            return render_template('register.html', message=message)
    return render_template('register.html')

# Endpoint for retrivieng password
@app.route('/retpass', methods=['GET', 'POST'])
def retpass():
    message = None
    # Load data
    df_logins = pd.read_csv(credentials/'login_credentials.csv')
    if request.method == 'POST':
        email = request.form['email']
        user = df_logins.email.isin([str(email)]).any()
        if user:
            msg = Message("Your Password Retrieval Requst..",
                          sender="admin@attendance.lsbu.ac.uk", recipients=[email])
            msg.body = "Hi,\n\nThanks for your password retirval request!\n\nYour password is: " +\
                df_logins.loc[df_logins.email==email, 'password'].astype(str).values[0] + "\n\nThanks for using our service.\n\nRegards,\nAdmin Team"
            mail.send(msg)
            message = "Password sent to " + email
            return render_template('retpass.html', message=message)
        elif request.form['email'] == '':
            message = 'Email is required!'
            return render_template('retpass.html', message=message)
        else:
            message = "This email doesn't exist. Please create an account."
            return render_template('retpass.html', message=message)
    return render_template('retpass.html')

# Endpoint for home
@app.route('/home')
@login_required
def home():
    user_name = current_user.username
    df = pd.read_csv(processed/'weekly_attendance.csv')
    df.course_code = df.course_code.astype(str)
    df.academic_semester = df.academic_semester.astype(str)

    rect = alt.Chart(df).mark_rect().encode(
        alt.X('course_code', bin=False, title='Course Code'),
        alt.Y('total_attendees', bin=False, title='Total Attendance (Weekly)'),
        alt.Color('total_attendees',
                scale=alt.Scale(scheme='greenblue'),
                legend=alt.Legend(title='Total Attendees')
                )
    ).properties(height=500, width=578, title='Total Attendees (Weekly) by Course')

    circ = rect.mark_point().encode(
        alt.ColorValue('grey'),
        alt.Size('total_attendees',
                legend=alt.Legend(title='Total Attendees')
                ))

    chart1 = alt.vconcat(
        rect + circ
    ).resolve_legend(
        color="independent",
        size="independent"
    )

    chart2 = alt.Chart(df).mark_circle(size=200).encode(
        x=alt.X('course_code', title='Course Code'),
        y=alt.Y('total_attendees', title='Total Attendance (Weekly)'),
        color=alt.Color('academic_semester', title='Semester'),
        tooltip=['course_code', 'course_name', 'month', 'year', 'academic_semester', 'academic_week', 'total_attendees']
    ).interactive().properties(height=500,
                            width=578, title='Total Attendees (Weekly) by Course')

    (chart1 | chart2).save('templates/charts.html')

    altair_bs = BeautifulSoup(
        open('templates/charts.html').read(), 'html.parser')

    altair_script = altair_bs.find_all('script')[-1].contents[0]

    chart_id = altair_bs.find('body').div['id']

    with open('static/plots.js', 'w')as f:
        f.write(altair_script)
        f.close()

    return render_template('home.html', chart_id=chart_id, user_name=user_name)


# Endpoint for about
@app.route('/about')
@login_required
def about():
    return render_template('about.html')

# Endpoint for contact
@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')


# Endpoint for Student Table
@app.route('/table1', methods=['GET'])
@login_required
def table1():  
    df = pd.read_csv(credentials/'students.csv').dropna()
    
    headings = df.columns.values
    headings = tuple(headings)

    data = df.to_records(index=False)
    data = tuple(data)
    return render_template('table1.html', headings=headings, data=data)


# Endpoint for Admin Table
@app.route('/table2', methods=['GET'])
@login_required
def table2():  # put application's code here

    df = pd.read_csv(credentials/'admins.csv').dropna()

    headings = df.columns.values
    headings = tuple(headings)

    data = df.to_records(index=False)
    data = tuple(data)
    return render_template('table2.html', headings=headings, data=data)

# Endpoint for Course Table
@app.route('/table3', methods=['GET'])
@login_required
def table3():  # put application's code here

    df = pd.read_csv(credentials/'courses.csv').dropna()

    headings = df.columns.values
    headings = tuple(headings)

    data = df.to_records(index=False)
    data = tuple(data)
    return render_template('table3.html', headings=headings, data=data)

# Endpoint for Timetable Table
@app.route('/table4', methods=['GET'])
@login_required
def table4():  # put application's code here

    df = pd.read_csv(credentials/'timetable.csv').dropna()

    headings = df.columns.values
    headings = tuple(headings)

    data = df.to_records(index=False)
    data = tuple(data)
    return render_template('table4.html', headings=headings, data=data)

# Endpoint for Attendance Statistics Table
@app.route('/table5', methods=['GET'])
@login_required
def table5():  # put application's code here

    df = pd.read_csv(processed/'weekly_attendance.csv').dropna()

    headings = df.columns.values
    headings = tuple(headings)

    data = df.to_records(index=False)
    data = tuple(data)
    return render_template('table5.html', headings=headings, data=data)

# Endpoint for adding new students
@app.route('/add_students', methods=['GET', 'POST'])
@login_required
def add_students():  
    message = None
    df_students = pd.read_csv(credentials/'students.csv')
    if request.method == 'POST':
        id =len(df_students)+1
        student_id = request.form['student_id']
        test = df_students.student_id.astype(str).isin([str(student_id)]).any()
        if test:
            message = 'Student ID exists! Please check the Student ID, or contact the administrator.'
            return render_template('add_students.html', message=message)
        if request.form['first_name'] == '':
            message = 'First Name is required!'
            return render_template('add_students.html', message=message)
        elif request.form['last_name'] == '':
            message = 'Last Name is required!'
            return render_template('add_students.html', message=message)
        elif request.form['student_id'] == '':
            message = 'Student ID is required!'
            return render_template('add_students.html', message=message)
        elif request.form['email'] == '':
                message = 'Email is required!'
                return render_template('add_students.html', message=message)
        elif ((str(request.form['student_id']).isdigit())==False) or (len(request.form['student_id'])!=6):
            message = 'Student ID must be 6 digits!'
            return render_template('add_students.html', message=message)
        elif str(request.form['email']).endswith('@lsbu.ac.uk')==False: 
            message = 'Invalid Email! Please type a valid LSBU email.'
            return render_template('add_students.html', message=message)
        elif df_students.email.isin([str(request.form['email'])]).any(): 
                message = 'Student Exists! Please add a different Student.'
                return render_template('add_students.html', message=message)
        else:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            student_id = request.form['student_id']
            email = request.form['email']
            
            df = df_students.append({'id': id, 'first_name': first_name, 'last_name': last_name, 'student_id': student_id,
            'email':email}, ignore_index=True)
            df.to_csv(credentials/'students.csv', index=False)
            message = "Thanks for adding a new student!"
            return render_template('add_students.html', message=message)
    return render_template('add_students.html')

# Endpoint for adding new tutors
@app.route('/add_tutors', methods=['GET', 'POST'])
@login_required
def add_tutors():  
    message = None
    df_admins = pd.read_csv(credentials/'admins.csv')
    id =len(df_admins)+1
    if request.method == 'POST':
        if request.form['first_name'] == '':
            message = 'First Name is required!'
            return render_template('add_tutors.html', message=message)
        elif request.form['last_name'] == '':
            message = 'Last Name is required!'
            return render_template('add_tutors.html', message=message)
        elif request.form['email'] == '':
            message = 'Email is required!'
            return render_template('add_tutors.html', message=message)
        elif str(request.form['email']).endswith('@lsbu.ac.uk')==False: 
            message = 'Invalid Email! Please type a valid LSBU email.'
            return render_template('add_tutors.html', message=message)
        elif df_admins.email.isin([str(request.form['email'])]).any(): 
            message = 'Tutor Exists! Please add a different tutor.'
            return render_template('add_tutors.html', message=message)
        else:
            try:
                test = df_admins.loc[df_admins.email==current_user.email, 'admin_status'].values[0]=='Yes'
            except:
                message = 'This Account does not have the admin rights to add a new tutor. Please contact the system admin.'
                return render_template('add_tutors.html', message=message)
            if test:
                first_name = request.form['first_name']
                last_name = request.form['last_name']
                email = request.form['email']
                
                df = df_admins.append({'id': id, 'first_name': first_name, 'last_name': last_name, 'email': email, 
                'description': 'Tutor', 'admin_status': 'No'}, ignore_index=True)
                df.to_csv(credentials/'admins.csv', index=False)
                message = "Thanks for adding a new tutor!"
                return render_template('add_tutors.html', message=message)
            else:
                message = 'This Account does not have the admin rights to add a new tutor. Please contact the system admin.'
                return render_template('add_tutors.html', message=message) 
    return render_template('add_tutors.html')

# Endpoint for adding new courses
@app.route('/add_course', methods=['GET', 'POST'])
@login_required
def add_course():  
    message = None
    df_admins = pd.read_csv(credentials/'admins.csv')
    df_courses = pd.read_csv(credentials/'courses.csv')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = [f'{i:02d}:{0:02d}' for i in range(9,19)]
    length = range(1, 4)
    id_courses =len(df_courses)+1
    id_admins = len(df_admins)+1
    if request.method == 'POST':
        if request.form['course_name'] == '':
            message = 'Course Name is required!'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        elif request.form['tutor_name'] == '':
            message = 'Tutor Name is required!'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        elif request.form['email'] == '':
            message = 'Email is required!'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        elif str(request.form['email']).endswith('@lsbu.ac.uk')==False: 
            message = 'Invalid Email! Please type a valid LSBU email.'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        elif len(str(request.form['tutor_name']).split(' ')) == 1:
            message = 'Tutor Name should at least contain the firstname and surname'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        elif df_courses.course_name.isin([str(request.form['course_name'])]).any(): 
            message = 'Course Exists! Please add a different Course.'
            return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
        else:
            try:
                test = df_admins.loc[df_admins.email==current_user.email, 'admin_status'].values[0]=='Yes'
            except:
                message = 'This Account does not have the admin rights to add a new course. Please contact the system admin.'
                return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
            if test:
                course_name = request.form['course_name']
                course_code = df_courses.course_code.max()+1
                tutor = request.form['tutor_name']
                email = request.form['email']
                teaching_day = request.form['teaching_day']
                start_time = request.form['start_time']
                duration = request.form['duration']
                end_time = (pd.to_datetime(pd.Series([f'{start_time}'])) + pd.Timedelta(f"{duration} hour")).dt.strftime('%H:%M')[0]
                
                df_courses = df_courses.append({'id': id_courses, 'course_name': course_name, 'course_code': course_code, 'tutor': tutor, 
                'email': email, 'teaching_day': teaching_day, 'start_time': start_time, 'end_time': end_time}, ignore_index=True)
                df_courses.to_csv(credentials/'courses.csv', index=False)
                message = f"Thanks for adding a new course! The course code is: {int(course_code)}."

                if not(df_admins.email.isin([email]).any()):
                    df_admins = df_admins.append({'id': id_admins, 'first_name': str(tutor).split()[0], 'last_name': str(tutor).split()[1],
                    'email': email, 'description': 'Tutor', 'admin_status': 'No'}, ignore_index=True)
                    df_admins.to_csv(credentials/'admins.csv', index=False)
                return render_template('add_new_course.html', message=message, days=days, times=times, length=length)
            else:
                message = 'This Account does not have the admin rights to add a new course. Please contact the system admin.'
                return render_template('add_new_course.html', message=message, days=days, times=times, length=length) 
    return render_template('add_new_course.html', days=days, times=times, length=length)

# Endpoint for updating a courses
@app.route('/update_course', methods=['GET', 'POST'])
@login_required
def update_course():  
    message = None
    df_admins = pd.read_csv(credentials/'admins.csv')
    df_courses = pd.read_csv(credentials/'courses.csv')
    courses = df_courses.course_name.dropna().unique()
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = [f'{i:02d}:{0:02d}' for i in range(9,19)]
    length = range(1, 4)

    if request.method == 'POST':
        try:
            test = df_admins.loc[df_admins.email==current_user.email, 'admin_status'].values[0]=='Yes'
        except:
            message = 'This Account does not have the admin rights to update a course. Please contact the system admin.'
            return render_template('update_course.html', message=message, courses=courses, days=days, times=times, length=length)
        if test:
            course_name = request.form['comp_select']
            teaching_day = request.form['comp_select1']
            start_time = request.form['comp_select2']
            duration = request.form['comp_select3']
            end_time = (pd.to_datetime(pd.Series([f'{start_time}'])) + pd.Timedelta(f"{duration} hour")).dt.strftime('%H:%M').squeeze()

            index = df_courses.loc[df_courses.course_name==course_name].index.values[0]

            df_courses.loc[index, 'teaching_day'] = teaching_day
            df_courses.loc[index, 'start_time'] = start_time
            df_courses.loc[index, 'end_time'] = end_time
            df_courses.to_csv(credentials/'courses.csv', index=False)

            message = f"Thanks for updating the course '{course_name}.' Please go to the 'Course List' to check the changes." 
            return render_template('update_course.html', message=message, courses=courses, days=days, times=times, length=length)
        else:
            message = 'This Account does not have the admin rights to update a course. Please contact the system admin.'
            return render_template('update_course.html', message=message, courses=courses, days=days, times=times, length=length)
    return render_template('update_course.html', courses=courses, days=days, times=times, length=length)

# Endpoint for creating new timetable
@app.route('/create_timetable', methods=['GET', 'POST'])
@login_required
def create_timetable():  
    message = None
    df_admins = pd.read_csv(credentials/'admins.csv')

    years =  [str(date.today().year-1)+'-'+str(date.today().year)[2:], str(date.today().year)+'-'+str(date.today().year+1)[2:]]
    year_dict = {str(date.today().year-1)+'-'+str(date.today().year)[2:]: [date.today().year-1, date.today().year], str(date.today().year)+'-'+str(date.today().year+1)[2:]: [date.today().year, date.today().year+1]}

    if request.method == 'POST':
        year = request.form['year']
        year_1 = year_dict[year][0]
        year_2 = year_dict[year][1]

        total_academcic_week = int(request.form['total_weeks'])
        sem1_start = request.form['sem1_start']
        sem2_start = request.form['sem2_start']
        number_of_holiday_week1 = int(request.form['holiday_week1'])
        number_of_holiday_week2 = int(request.form['holiday_week2'])
        sem1_holiday_start = request.form['sem1_holiday_start']
        sem2_holiday_start = request.form['sem2_holiday_start']

        m = re.fullmatch('\d{4,4}-\d{2,2}-\d{2,2}', sem1_start)
        n = m = re.fullmatch('\d{4,4}-\d{2,2}-\d{2,2}', sem2_start)
        m_ = re.fullmatch('\d{4,4}-\d{2,2}-\d{2,2}', sem1_holiday_start)
        n_ = re.fullmatch('\d{4,4}-\d{2,2}-\d{2,2}', sem2_holiday_start)

        if sem1_start == '':
            message = message = 'Semester 1 Start Date is required!'
            return render_template('create_timetable.html', message=message, years=years)
        if sem1_holiday_start == '':
            message = message = 'Semester 2 Holiday Start Date is required!'
            return render_template('create_timetable.html', message=message, years=years)
        elif sem2_start == '':
            message = message = 'Semester 2 Start Date is required!'
            return render_template('create_timetable.html', message=message, years=years)
        elif sem2_holiday_start == '':
            message = message = 'Semester 2 Holiday Start Date is required!'
            return render_template('create_timetable.html', message=message, years=years)
        elif m == None:
            message = message = 'Semester 1 Start Date must be in \'YYYY-MM-DD\' format!'
            return render_template('create_timetable.html', message=message, years=years)
        elif m_ == None:
            message = message = 'Semester 1 Holiday Start Date must be in \'YYYY-MM-DD\' format!'
            return render_template('create_timetable.html', message=message, years=years)
        elif n == None:
            message = message = 'Semester 2 Start Date must be in \'YYYY-MM-DD\' format!'
            return render_template('create_timetable.html', message=message, years=years)
        elif n_ == None:
            message = message = 'Semester 2 Holiday Start Date must be in \'YYYY-MM-DD\' format!'
            return render_template('create_timetable.html', message=message, years=years)
        else:
            m_year = int(sem1_start[:4])
            m_month = int(sem1_start[5:7])
            m_year_ = int(sem1_holiday_start[:4])
            m_month_ = int(sem1_holiday_start[5:7])
            n_year = int(sem2_start[:4])
            n_month = int(sem2_start[5:7])
            n_year_ = int(sem2_holiday_start[:4])
            n_month_ = int(sem2_holiday_start[5:7])
            if m_year != year_1 or m_month != 9:
                message = message = f"Semester 1 Start Date must be in 'September' {year_1}!"
                return render_template('create_timetable.html', message=message, years=years)
            elif m_year_ != year_1 or m_month_ != 12:
                message = message = f"Semester 1 Holiday Start Date must be in 'December' {year_1}!"
                return render_template('create_timetable.html', message=message, years=years)
            if n_year != year_2 or n_month != 1:
                message = message = f"Semester 2 Start Date must be in 'January' {year_2}!"
                return render_template('create_timetable.html', message=message, years=years)
            elif n_year_ != year_2 or n_month_ != 4:
                message = message = f"Semester 2 Holiday Start Date must be in 'April' {year_2}!"
                return render_template('create_timetable.html', message=message, years=years)
            else:
                df_date = pd.DataFrame(pd.period_range(start=date(year_1, 9, 1), end=date(year_2, 6, 30), freq='W'), columns=['date_range'])
                df_date['month'] = df_date.date_range.dt.start_time.dt.month

                df1 = df_date.loc[df_date[df_date.date_range.dt.start_time.dt.date.astype(str) == sem1_start].index.values[0]:, ['date_range']].reset_index(drop=True)
                df2 = df_date.loc[df_date[df_date.date_range.dt.start_time.dt.date.astype(str) == sem2_start].index.values[0]:, ['date_range']].reset_index(drop=True)

                last_academic_week1 = df1[df1.date_range.dt.start_time.dt.date.astype(str) == sem1_holiday_start].index.values[0]
                last_academic_week2 = df2[df2.date_range.dt.start_time.dt.date.astype(str) == sem2_holiday_start].index.values[0]
                
                df1 = pd.concat([df1.loc[:last_academic_week1-1], df1.loc[last_academic_week1+number_of_holiday_week1:]]).reset_index(drop=True).loc[:total_academcic_week-1]
                df2 = pd.concat([df2.loc[:last_academic_week2-1], df2.loc[last_academic_week2+number_of_holiday_week2:]]).reset_index(drop=True).loc[:total_academcic_week-1]

                df1['academic_semester'] = 1
                df1['academic_week'] = df1.index+1
                df1['calendar_week'] = df1.date_range.dt.start_time.dt.week
                df1['week_start'] = df1.date_range.dt.start_time.dt.date
                df1['week_end'] = df1.date_range.dt.end_time.dt.date

                df1 = df1[['academic_semester', 'academic_week', 'calendar_week', 'date_range', 'week_start', 'week_end']]
                
                df2['academic_semester'] = 2
                df2['academic_week'] = df2.index+1
                df2['calendar_week'] = df2.date_range.dt.start_time.dt.week
                df2['week_start'] = df2.date_range.dt.start_time.dt.date
                df2['week_end'] = df2.date_range.dt.end_time.dt.date

                df2 = df2[['academic_semester', 'academic_week', 'calendar_week', 'date_range', 'week_start', 'week_end']]

                df = pd.concat([df1, df2], ignore_index=True)
                try:
                    test = df_admins.loc[df_admins.email==current_user.email, 'admin_status'].values[0]=='Yes'
                except:
                    message = 'This Account does not have the admin rights to create a new timetable. Please contact the system admin.'
                    return render_template('create_timetable.html', message=message, years=years)
                if test:
                    df.to_csv(credentials/f'timetable.csv', index=False)
                    message = 'Thanks for creating a new timetable! Please check the timetable on the Check Timetable page.'
                    return render_template('create_timetable.html', message=message, years=years)
                else:
                    message = 'This Account does not have the admin rights to create a new timetable. Please contact the system admin.'
                    return render_template('create_timetable.html', message=message, years=years)
    return render_template('create_timetable.html', message=message, years=years)

# Endpoint for creating attendance
@app.route('/create_attendance', methods=['GET', 'POST'])
@login_required
def create_attendance():  
    message = None
    df_students = pd.read_csv(credentials/'students.csv')
    df_courses = pd.read_csv(credentials/'courses.csv')
    df_timetable = pd.read_csv(credentials/'timetable.csv', parse_dates=['week_start', 'week_end'], infer_datetime_format=True)
    courses = df_courses.course_name.dropna().unique()
    weeks = list(df_timetable.academic_week.dropna().unique())

    days_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    if request.method == 'POST':
        course_name =request.form['comp_select']
        course_code = df_courses.loc[df_courses.course_name == course_name, 'course_code'].squeeze()
        semester = int(request.form['comp_select1'])
        academic_week = int(request.form['comp_select2'])

        file_name = f'{course_code}_semester_{semester}_week_{academic_week}_attendance.csv'

        if (processed/'attendance'/file_name).exists():
            message = f"Attendance for '{course_name}' for 'semester {semester}', 'week {academic_week}' already exists! Please go to the 'Check Attendance' page to check the attendance."
            return render_template('create_attendance.html', message=message, courses=courses, weeks=weeks)

        else:
            teaching_day = df_courses.loc[df_courses.course_name == course_name, 'teaching_day'].squeeze()
            day_num_in_week = days_dict[teaching_day]

            week_start = df_timetable.loc[(df_timetable.academic_semester==semester) & (df_timetable.academic_week==academic_week), 'week_start'] 
            year = (week_start + pd.DateOffset(days=day_num_in_week)).dt.year.squeeze()
            month = (week_start + pd.DateOffset(days=day_num_in_week)).dt.month.squeeze()
            month_name = (week_start + pd.DateOffset(days=day_num_in_week)).dt.month_name().squeeze()
            week = (week_start + pd.DateOffset(days=day_num_in_week)).dt.week.squeeze()
            day = (week_start + pd.DateOffset(days=day_num_in_week)).dt.day.squeeze()
            day_name = (week_start + pd.DateOffset(days=day_num_in_week)).dt.day_name().squeeze()
            date = (week_start + pd.DateOffset(days=day_num_in_week)).dt.date.squeeze()
            start_hour = int(df_courses.loc[df_courses.course_name == course_name, 'start_time'].apply(lambda x: str(x)[:2]).squeeze())
            end_hour = int(df_courses.loc[df_courses.course_name == course_name, 'end_time'].apply(lambda x: str(x)[:2]).squeeze())
            
            # Retrieve sms using the client object
            messages = client.messages.list(
                date_sent_after=datetime(year, month, day, start_hour, 0, 0),
                date_sent_before=datetime(year, month, day, end_hour, 0, 0)
            )
            if len(messages) == 0:
                message = 'No attendance received for that week!'
                return render_template('create_attendance.html', message=message, courses=courses, weeks=weeks)
            else:
                # Append the retrieved sms's to a dataframe
                d = []
                for message in messages:
                    d.append((message.from_, message.body, message.status, message.date_sent))

                df = pd.DataFrame(d, columns=['from' ,'message' ,'status' ,'date_sent'])
                try:
                    df['student_id'] = df.message.str.split(' ', expand=True, n=1)[0]
                except:
                    df['student_id'] = None
                try:
                    df['course_code'] = df.message.str.split(' ', expand=True, n=1)[1]
                except:
                    df['course_code'] = None
                
                # function to extract student name
                def student_name(df):
                    first_name = df_students.loc[df_students.student_id.astype(str) == df.student_id, 'first_name'].squeeze()
                    last_name = df_students.loc[df_students.student_id.astype(str) == df.student_id, 'last_name'].squeeze()
                    df['student_name'] = first_name+ ' ' + last_name
                    return df

                df = df.loc[df.status=='received'].apply(student_name, axis='columns')

                df_attendance = df.loc[(df.student_id.isin(df_students.student_id.astype(str))) & (df.course_code==str(course_code))]
                df_attendance = df_attendance[['from', 'student_id', 'student_name', 'message', 'date_sent']]
                df_invalid_attendance = df.loc[~(df.student_id.isin(df_students.student_id.astype(str))) | (df.course_code!=str(course_code))]
                
                file_name_raw = f'{course_code}_semester_{semester}_week_{academic_week}_raw.csv'
                file_name_spam = f'{course_code}_semester_{semester}_week_{academic_week}_spammed.csv'

                df.to_csv(raw/file_name_raw, index=False)
                df_attendance.to_csv(processed/'attendance'/file_name, index=False)
                df_invalid_attendance.to_csv(processed/'spam'/file_name_spam, index=False)

                df_weekly = pd.read_csv(processed/'weekly_attendance.csv')

                df_weekly = df_weekly.append({
                    'course_name': course_name, 'course_code': course_code, 'date': date, 'year': year, 'month': month_name,
                    'day': day_name, 'week': week, 'academic_semester': semester, 'academic_week': academic_week, 'total_attendees': len(df_attendance)
                }, ignore_index=True)
                df_weekly.to_csv(processed/'weekly_attendance.csv', index=False)
                
                # Acknowledgement message to the students
                for student in df_attendance.student_id:
                    student_name = df_students.loc[df_students.student_id.astype(str).isin([student]), 'first_name'].squeeze()
                    student_phone_no = df_attendance.loc[df_attendance.student_id==student, 'from'].squeeze()

                    client.messages.create(
                    body = f"Hi {student_name}, congratulations! Your attendance for '{course_name}', 'semester {semester}', 'week {academic_week}' has been successfully registered.",
                    from_ = os.environ.get("TWILIO_PHONE_NUMBER"),
                    to=student_phone_no)
                
                # Email the attendance to the tutor
                tutor_name = df_courses.loc[df_courses.course_name == course_name, 'tutor'].str.split(' ', expand=True, n=1)[0].squeeze()
                tutor_email = df_courses.loc[df_courses.course_name == course_name, 'email'].squeeze()
                msg = Message(f'Attendance- {course_name}, semester {semester}, week {academic_week}',
                          sender="admin@attendance.lsbu.ac.uk", recipients=[tutor_email])
                msg.body = f"Hi {tutor_name},\n\nThe attendance for '{course_name}' for 'semester {semester}', 'week {academic_week}' has been created.\n\nPlease find the attendance attached!\n\nKind Regards,\nAttendance Team"
                with app.open_resource(f'datasets\\processed\\attendance\\{file_name}') as fp:  
                    msg.attach(f'datasets\\processed\\attendance\\{file_name}', "text/csv", fp.read()) 
                mail.send(msg)

                message = f"Attendance for '{course_name}' for 'semester {semester}', 'week {academic_week}' created successfully! Please go to the 'Check Attendance' page to check the attendance."
                return render_template('create_attendance.html', message=message, courses=courses, weeks=weeks)
    return render_template('create_attendance.html', courses=courses, weeks=weeks)

# Endpoint for showing attendance
@app.route('/check_attendance', methods=['GET', 'POST'])
@login_required
def check_attendance():  
    message = None
    df_courses = pd.read_csv(credentials/'courses.csv')
    df_timetable = pd.read_csv(credentials/'timetable.csv', parse_dates=['week_start', 'week_end'], infer_datetime_format=True)
    courses = df_courses.course_name.dropna().unique()
    weeks = list(df_timetable.academic_week.dropna().unique())

    if request.method == 'POST':
        course_name =request.form['comp_select']
        course_code = df_courses.loc[df_courses.course_name == course_name, 'course_code'].squeeze()
        semester = int(request.form['comp_select1'])
        academic_week = int(request.form['comp_select2'])

        file_name = f'{course_code}_semester_{semester}_week_{academic_week}_attendance.csv'

        if (processed/'attendance'/file_name).exists():
        
            df = pd.read_csv(processed/'attendance'/file_name).dropna()
            headings = df.columns.values
            headings = tuple(headings)

            data = df.to_records(index=False)
            data = tuple(data)
            return render_template('table6.html', headings=headings, data=data, course_name=course_name, semester=semester, academic_week=academic_week)
        else:
            message = f"No attendance found for '{course_name}', 'semester {semester}', 'week {academic_week}'! Please go to the 'Create Attendance' page to create an attendance."
            return render_template('check_attendance.html', message=message, courses=courses, weeks=weeks)
    return render_template('check_attendance.html', message=message, courses=courses, weeks=weeks)

# Endpoint for showing spammed attendance
@app.route('/check_spams', methods=['GET', 'POST'])
@login_required
def check_spams():  
    message = None
    df_courses = pd.read_csv(credentials/'courses.csv')
    df_timetable = pd.read_csv(credentials/'timetable.csv', parse_dates=['week_start', 'week_end'], infer_datetime_format=True)
    courses = df_courses.course_name.dropna().unique()
    weeks = list(df_timetable.academic_week.dropna().unique())

    if request.method == 'POST':
        course_name =request.form['comp_select']
        course_code = df_courses.loc[df_courses.course_name == course_name, 'course_code'].squeeze()
        semester = int(request.form['comp_select1'])
        academic_week = int(request.form['comp_select2'])

        file_name_spam = f'{course_code}_semester_{semester}_week_{academic_week}_spammed.csv'

        if (processed/'spam'/file_name_spam).exists():
        
            df = pd.read_csv(processed/'spam'/file_name_spam).dropna(how='all')
            headings = df.columns.values
            headings = tuple(headings)

            data = df.to_records(index=False)
            data = tuple(data)
            return render_template('table7.html', headings=headings, data=data, course_name=course_name, semester=semester, academic_week=academic_week)
        else:
            message = f"No spams found for '{course_name}', 'semester {semester}', 'week {academic_week}'! Please go to the 'Create Attendance' page to create an attendance."
            return render_template('check_spams.html', message=message, courses=courses, weeks=weeks)
    return render_template('check_spams.html', message=message, courses=courses, weeks=weeks)

# Endpoint for displaying phone number
@app.route('/display_number', methods=['GET', 'POST'])
@login_required
def display_number():  
    message = None
    df_courses = pd.read_csv(credentials/'courses.csv')
    courses = df_courses.course_name.dropna().unique()
    number = os.environ.get('TWILIO_PHONE_NUMBER')
    if request.method == 'POST':
        course_name =request.form['comp_select']
        course_code = df_courses.loc[df_courses.course_name == course_name, 'course_code'].squeeze()
        start_time = df_courses.loc[df_courses.course_name == course_name, 'start_time'].squeeze()
        end_time = df_courses.loc[df_courses.course_name == course_name, 'end_time'].squeeze()
        duration = f'{start_time}-{end_time}'
        return render_template('display_number.html', message=message, courses=courses, course_code=course_code, duration=duration, number=number)
    return render_template('display_number.html', message=message, courses=courses)

# Endpoint for sending reminder
@app.route('/send_reminder', methods=['GET', 'POST'])
@login_required
def send_reminder():  
    message = None
    df_courses = pd.read_csv(credentials/'courses.csv')
    courses = df_courses.course_name.dropna().unique()
    number = os.environ.get('TWILIO_PHONE_NUMBER')
    if request.method == 'POST':
        course_name =request.form['comp_select']
        course_code = df_courses.loc[df_courses.course_name == course_name, 'course_code'].squeeze()
        start_time = df_courses.loc[df_courses.course_name == course_name, 'start_time'].squeeze()
        end_time = df_courses.loc[df_courses.course_name == course_name, 'end_time'].squeeze()
        duration = f'{start_time}-{end_time}'

        file_name = f'{course_code}_enrolled_students.csv'
        
        df_students = pd.read_csv(credentials/'enrolled'/file_name)
        for i in range(len(df_students)):
            msg = Message(f"Attendance Reminder '{course_name}'...",
                          sender="admin@attendance.lsbu.ac.uk", recipients=[df_students.email[i]])
            msg.body = f"Hi {df_students.first_name[i]},\n\nPlease kindly register your attendance for '{course_name}' between {duration}.\n\nPlease kindly quote: '{df_students.student_id[i]} {course_code}' in your SMS and send to '{number}.'\n\nYou will receive an acknowledgment later for your attendance.\n\nShould you require any assistance, please contact your tutor.\n\nKind Regards,\nAttendance Team"
            mail.send(msg)
        message = f"Reminder sent for '{course_name}!'" 
        return render_template('send_reminder.html', message=message, courses=courses)
    return render_template('send_reminder.html', message=message, courses=courses)


if __name__ == '__main__':
    app.run(debug=True)
