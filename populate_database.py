import os
import pandas as pd
import psycopg2
from datetime import datetime
from db_config import DATABASE_PARAMS

# let's preprocess and standardize date formats
def preprocess_dates(df, date_column, current_format=None, target_format='%Y-%m-%d %H:%M:%S'):
    if current_format:
        df[date_column] = pd.to_datetime(df[date_column], format=current_format)
    else:
        df[date_column] = pd.to_datetime(df[date_column])
    df[date_column] = df[date_column].dt.strftime(target_format)
    return df

def clean_mobile_number(mobile):
    mobile_str = str(mobile).strip('"')
    
    # check if it already fits the desired format: 9 digits and starts with 5
    if len(mobile_str) == 9 and mobile_str.startswith('5'):
        return mobile_str
    
    # extract the last 9 digits
    last_nine = mobile_str[-9:]
    return last_nine if last_nine.startswith('5') else mobile_str

data_folder = './data/'

conn = psycopg2.connect(**DATABASE_PARAMS)
cur = conn.cursor()

csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# process for each file
for file_name in csv_files:
    file_path = os.path.join(data_folder, file_name)
    df = pd.read_csv(file_path)
    
    # get the status and date format based on the file name
    if "Pickup" in file_name:
        status, date_format = "pickup", '%d-%m-%Y %I:%M %p'
    elif "Delivery_exceptions" in file_name:
        status, date_format = "delivery_exception", '%d-%m-%Y %H:%M'
    elif "Delivered" in file_name:
        status, date_format = "delivered", None
    elif "Returned" in file_name:
        status, date_format = "returned", '%d-%m-%Y %I:%M%p'
    else:
        continue
    if 'User contact' in df.columns:
        df.rename(columns={'User contact': 'User Mobile'}, inplace=True)
    
    df = preprocess_dates(df, 'Timestamp', current_format=date_format)
    df['User Mobile'] = df['User Mobile'].apply(clean_mobile_number)
    
    # insert data into the database
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO card_status_table (card_id, user_mobile, timestamp, status, comment) VALUES (%s, %s, %s, %s, %s)",
            (row['Card ID'], row['User Mobile'], row['Timestamp'], status, row.get('Comment', None))
        )

conn.commit()
cur.close()
conn.close()

print("Data imported successfully.")
