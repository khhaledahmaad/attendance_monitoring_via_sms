![lsbu%20logo.png](attachment:lsbu%20logo.png)

## Configuartion

Make sure you have `Python`, and `Git` configured. If not please follow the link, [Python](https://www.python.org/downloads/), and the link [Git](https://git-scm.com/downloads) to download and install seperately.

The `requirements.txt` files lists all the pthon packages needed to run the application.

## Folder Structure
```python
|-- attendance_monioring_via_sms
|   |-- .twilio
|   |-- datasets
|      |-- *.csv
|   |-- docs
|      |-- *.md
|      |-- *.pdf
|   |-- env_vars
|      |-- .env.txt
|   |-- images
|      |-- *.png
|   |-- nbs
|      |-- *.ipynb 
|   |-- static
|      |- *.css
|      |- *.js
|   |-- templates
|      |- *.html
|   |-- app.py
|   |-- conda_env_twilio.yml
|   |-- requirements.txt

```

## Option 1: Running the application on `Conda Environment`

## Conda 
Conda is an open-source, cross-platform, language-agnostic package manager and environment management system.

### Installation
Conda distributions, e.g., `Anaconda`, `Minoconda` can be downloaded easily form their website directly through this link:
[Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

After installation the `Conda` prompt looks like the following:
![image.png](attachment:image.png)

### Download the Source Code

Open the `Conda` prompt and change to your preferred directory location and then try:

```python 
$ git clone git@github.com:khhaledahmaad/attendance_monitoring_via_sms.git
```

__N.B.:__ Please make sure you create and add an SSH Key to your account before using the above command. Please follow this [link](https://github.com/khhaledahmaad/attendance_monitoring_via_sms/blob/main/docs/GitHub_SSHKey.pdf) for configuring SSH access to repositories.

If this command does not work in your setup, simply download the `ZIP` file of the source code by pressing `<> Code > Local > Download ZIP` and extract it to the prefered directory.

Now that you have the source code folder, change to the location of that cloned directory, and then run the following commands:

```python
$ cd attendance_monitoring_via_sms
```

```python
$ conda env create --file conda_env_twilio.yml
```

```python
$ conda activate twilio
```

After making any change in the applicaton, i.e., adding new fetures, packages or whatsoever, please use the following command to update the conda and pip dependencies accordingly:

```python
$ conda env export > conda_env_twilio.yml
```

### Run the Application

Simply run the following command after creating and activating the conda environment:

```python
$ python app.py
```

Follow the link on the console, saying `*Running on` or simply copy-paste in a browser, which will take to the `Flask` application running on the local server.
![image.png](attachment:image.png)

## Option 2: Running the application on Python  Virtual Environment (venv)

### venv
The module used to create and manage virtual environments is called venv. venv will usually install the most recent version of Python that you have available. If you have multiple versions of Python on your system, you can select a specific Python version by running python3 or whichever version you want.

virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.

### Installation
virtualenv can be downloaded and installed by following the description throght the link, 
[pip-venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) or by simply using the command in a command prompt, provided that `Python` and `Pip` are already installed.

```python
$ pip install virtualenv
```

## Download the Source Code
Open the `Command Prompt` or the terminal of your desired code editor/IDE, e.g., `VS Code` and change to your preferred directory location and then try:

```python 
$ git clone git@github.com:khhaledahmaad/attendance_monitoring_via_sms.git
```

__N.B.:__ Please make sure you create and add an SSH Key to your account before using the above command. Please follow this [link](https://github.com/khhaledahmaad/attendance_monitoring_via_sms/blob/main/docs/GitHub_SSHKey.pdf) for configuring SSH access to repositories.

If this command does not work in your setup, simply download the `ZIP` file of the source code by pressing `<> Code > Local > Download ZIP` and extract it to the prefered directory.

Now that you have the source code folder, change to the location of that cloned directory, and then run the following commands:

```python
$ cd attendance_monitoring_via_sms
```

```python
$ python -m venv .twilio
```

```python
$ .twilio\Scripts\activate
```

```python
$ pip install -r requirements.txt
```

After making any change in the applicaton, i.e., adding new fetures, packages or whatsoever, please use the following command to update the pip dependencies to the virtualenv accordingly:

```python
$ pip freeze > requirements.txt
```

### Run the Application

Simply run the following command after creating and activating the virtualenv:

```python
$ python app.py
```

Follow the link on the console, saying `*Running on` or simply copy-paste in a browser, which will take to the `Flask` application running on the local server.
![image.png](attachment:image.png)