# Import libraries
import os
import pathlib
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from twilio.rest import Client

# Set paths
# Path to all data directories
data = pathlib.Path(r'C:\Users\ahmedk40\Documents\GitHub\Attendance-Monitoring-via-SMS\data')

# Path to raw data
raw = data/'raw'

# Path to processed data
processed = data/'processed'

# Path to environment variables
env_vars = pathlib.Path(r'C:\Users\ahmedk40\Documents\GitHub\Attendance-Monitoring-via-SMS\env vars')

# Load environment variables from .env.txt file
load_dotenv(env_vars/".env.txt")

# Create twilio client object
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Retrieve sms using the client object
messages = client.messages.list(
    date_sent_after=datetime(2022, 11, 5, 12, 30, 0),
    date_sent_before=datetime(2022, 11, 5, 12, 40, 0)
)

# Append the retrieved sms's to a dataframe
d = []
for message in messages:
    d.append((message.from_, message.body ,message.status,message.date_sent))

df = pd.DataFrame(d ,columns=['from' ,'message' ,'status' ,'date_ent'])

# Preview
print(df.head())

# Export the dataframe to a CSV file
df.to_csv(raw/'smsLogs.csv', index=False, encoding='utf-8')