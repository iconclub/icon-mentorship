import json
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials

mentors = []
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1lOMM-RsbHL2sBaI-hk6GBuW6Ptc-qvjEb4HyiY2f2dc/edit#gid=1120776380").sheet1
# # Extract and print all of the values
records = sheet.get_all_records()
# reset
for idx, mentor in enumerate(data['mentors']):
    data['mentors'][idx]['soNguoiChon'] = 0

for record in records:
    print(record)
    idx = [idx for idx, mentor in enumerate(data['mentors']) if mentor['nickname'] == record['Chọn mentor']][0]
    data['mentors'][idx]['soNguoiChon'] += 1
    data['mentors'][idx]['soNguoiChon'] = 4 if data['mentors'][idx]['soNguoiChon'] >= 4 else data['mentors'][idx]['soNguoiChon']

data['update'] = str(time.time())

with open("data.json", "w") as json_file:
    json.dump(data, json_file, ensure_ascii=False)
