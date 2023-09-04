from os import access


import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
import csv

access_token = #accesstoken
user_id = #user id
heart_rate_request = requests.get('https://api.fitbit.com/1/user/user_id/activities/heart/date/2022-06-30/1d/1min/time/00:00/01:08.json', headers={'Authorization': 'Bearer ' + 'access_token'})


print(heart_rate_request.status_code)
data = heart_rate_request.json()['activities-heart-intraday']['dataset']
pprint(data)

#Save as CSV
with open("heartrate.csv", "w", newline= '') as csv_file:
    writer = csv.writer(csv_file, delimiter = ',')
    for line in data:
        print(line['value'])
        writer.writerow(line.values())
 
