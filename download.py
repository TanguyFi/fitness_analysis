import garminconnect
import os
import pandas as pd
from datetime import date, datetime
import itertools
from dotenv import load_dotenv
load_dotenv()

# Garmin credentials
login = os.getenv("GARMIN_LOGIN")
password = os.getenv("GARMIN_PASSWORD")

print(f'login: {login}')

garmin = garminconnect.Garmin(login, password)
garmin.login()

fullname = garmin.get_full_name()
print(f'fullname: {fullname}')

start_date = date(2023, 8, 1)
end_date = date(2023, 11, 30)

print(f'start_date: {start_date}')
print(f'end_date: {end_date}')

dates = pd.date_range(start_date, end_date, freq='d').strftime('%Y-%m-%d').tolist()

heart_rate_lists = []
timestamp_lists = []

print ('Downloading heart rate data...')

for day in dates:
    print(day)
    heart_rate_data = garmin.get_heart_rates(day)
    if heart_rate_data['heartRateValues'] is None: continue
    heart_rate_lists.append([i[1] for i in heart_rate_data['heartRateValues']])
    timestamp_lists.append([datetime.fromtimestamp(i[0]/1000) for i in heart_rate_data['heartRateValues']])

heart_rate_list = list(itertools.chain.from_iterable(heart_rate_lists))
timestamp_list = list(itertools.chain.from_iterable(timestamp_lists))

df = pd.DataFrame({'timestamp': timestamp_list, 'heart_rate': heart_rate_list})
df['timestamp'] = pd.to_datetime(df['timestamp'])

df = df.drop_duplicates(subset=['timestamp'], keep='first')
df = df.set_index('timestamp').resample('2min').ffill().reset_index()
df.sort_values(by='timestamp').to_csv('heart_rate.csv', index=False)
df.to_csv('heart_rate.csv', index=False)

print('Done! Data saved to heart_rate.csv')