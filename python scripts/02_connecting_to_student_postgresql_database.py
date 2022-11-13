#!/usr/bin/env python
# coding: utf-8

# ### Scope
# This notebook demonstrates how to connect to a postgresql database to read data into a dataframe.

# In[1]:


# Import libraries
import os
import pathlib
import pandas as pd
import psycopg2
from configparser import ConfigParser


# In[2]:


# Set paths

# Path to all data directories
data = pathlib.Path(r'C:\Users\ahmedk40\Documents\GitHub\Attendance-Monitoring-via-SMS\data')

# Path to raw data
raw = data/'raw'

# Path to processed data
processed = data/'processed'

# Path to environment variables
env_vars = pathlib.Path(r'C:\Users\ahmedk40\Documents\GitHub\Attendance-Monitoring-via-SMS\env vars')


# In[3]:


# create a parser
parser = ConfigParser()

"""
The following section reads a config file to load postgresql database credentials saved in a 'config.ini' file
"""

# read config file
parser.read(env_vars/'database.ini')

# get section, default to postgresql and append the database credentials into a dictionary
conn_string = {}
section = 'postgresql'
if parser.has_section(section):
    params = parser.items(section)
    for param in params:
        conn_string[param[0]] = param[1]


# In[4]:


try:
    # read connection parameters
    params = conn_string

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    # create a cursor
    cur = conn.cursor()

    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    
    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)

except (Exception, psycopg2.DatabaseError) as error:
    print(error)


# In[5]:


# Get all the schemas in the database
cur.execute('SELECT schema_name FROM information_schema.schemata')
schemas = [i[0] for i in cur.fetchall()] # A list() of schemas
schemas


# In[6]:


# Get all tables in the database
cur.execute("SELECT relname FROM pg_class WHERE relkind='r'AND relname !~ '^(pg_|sql_)';") # "rel" is short for relation.

tables = [i[0] for i in cur.fetchall()] # A list() of tables
tables


# In[7]:


# Read the 'studentCreds' table from the 'studentDB' schema into a dataframe
df = pd.read_sql('select * from "studentDB"."studentCreds";', conn)

# Preview
print(df.head())


# In[8]:


# Export the dataframe to a CSV file
df.to_csv(raw/'studentCreds.csv', index=False, encoding='utf-8')

