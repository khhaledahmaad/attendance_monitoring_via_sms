## Download the Source Code

Make sure you have python, conda and git configured in your corporate laptop. If not install please follow the [link](https://knorrbremse.service-now.com/self_service?id=kb_article&sys_id=b244d8f31b36641016f61f4c2e4bcbda) for python and conda and this [link](https://knorrbremse.service-now.com/self_service?id=kb_article&sys_id=541c9d8d1be3ec903c79520f6e4bcb4a) for git.

Once you have all the software mentioned above, just open the conda prompt and change to your preferred directory location and then try:

```python
git clone git@github.com:khhaledahmaad/dashboard.git
```
__N.B.:__ Please make sure you create and add an SSH Key to your account before using the above command. Please follow this [link](https://github.com/khhaledahmaad/dashboard/blob/main/GitHub_SSHKey.pdf) for configuring SSH access to repositories.

If this command does not work in your corporate setup, simply download the `ZIP` file.

![download](https://github.com/khhaledahmaad/dashboard/blob/main/images/download.png)

## Install the Conda Environment and Packages

Now that you have the source code folder, change to the location of that cloned directory, and then run the following commands:

```python
cd dashboard
```

```python
conda env create --file conda_env_dashboard.yml
```

```python
conda activate dashboard
```

After making any change in the applicaton, i.e., adding new fetures, packages or whatsoever, please use the following command to update the conda and pip dependencies accordingly:

```python
conda env export > conda_env_dashboard.yml
```

## Run the Application

Simply run the following command after creating and activating the conda environment:

```python
python app.py
```

If your default browser is not opened, open a browser and go to [localhost:8050](http://localhost:8050/). You should be able to create an account and login to the dashboard.

__N.B.:__ This application was designed in a MAC OS, and for this OS the best port is `8050`. If you are using a Windows OS, please use the default `Flask` port or port `5000`. 

## Log in (localhost:8050/)

The `Log in` page looks like the following:

![login](https://github.com/khhaledahmaad/dashboard/blob/main/images/login.png)

## Create New Account (localhost:8050/register)

The `Create New Account` page looks like the following:

![register](https://github.com/khhaledahmaad/dashboard/blob/main/images/register.png)


## Retrieve Password (localhost:8050/retpas)

You can retrieve your password in case forgotten. The `Forgotten Password` page looks like the following:

![retrieve password](https://github.com/khhaledahmaad/dashboard/blob/main/images/retrieve%20password.png)


This retrieval endpoint uses a dummy email testing tool in the `Flask` app, called [Mailtrap](https://mailtrap.io/). Please create free `Mailtrap` account and replace the `Mailtrap` credentials in the `Falsk` app to test the password retrieaval. The password retrieval eamils and the `Falsk-Mail` credentials for the account used to build this `Falsk` application is shown bellow:

![mailtrap](https://github.com/khhaledahmaad/dashboard/blob/main/images/flask%20email%20mailtrap.png)


__N.B.:__ Make sure you add all your credentials in the `.env.txt` file.

## Home Page(localhost:8050/home)

Once you have logged in, the home page opened is the main dashboard of this application, which shows all the real-time train tracking charts and maps as shown bellow:

![dashboard](https://github.com/khhaledahmaad/dashboard/blob/main/images/dashboard.png)


## Table1 (localhost:8050/table1)

This endpoint shows the tabular data in a sortable and filterable table. The data shown in this table is from the API response, therefore, live and get refreshed every time this endpoint is opened.

![table1](https://github.com/khhaledahmaad/dashboard/blob/main/images/table1.png)

## About (localhost:8050/about)

This endpoint simply depicts the feautures and tools used to build this application, also states some terms and conditions to use and deploy this application.

![about](https://github.com/khhaledahmaad/dashboard/blob/main/images/about.png)

## Contact (localhost:8050/contact)

This endpoint shows the copyright and contact information of Knorr-Bremse Rail Systems (UK) Ltd.

![contact](https://github.com/khhaledahmaad/dashboard/blob/main/images/contact.png)


## Conclusion

This dashboard was created with access to only one endpoint of the `ICOM REST API` that lists all the consists of `Scot Rail Class 334`. This dashboard demonstrates KB's internal capability to create such dashboards using internal resources to visualise and analyse customers' data as well as KB's own business  data.


__Thanks and regards:__ `Khaled Ahmed, Data Science Placement Student, 2021-22`

`Knorr-Bremse Rail Systems (UK) Ltd, Melksham SN12 6TL.`
