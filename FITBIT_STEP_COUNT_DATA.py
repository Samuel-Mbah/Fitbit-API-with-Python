from os import access


import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
import csv

access_token = 'access token'
user_id = 'user id'
activity_request = requests.get('https://api.fitbit.com/1/user/user_id/activities/steps/date/today/today.json',
                                headers={'Authorization': 'Bearer ' + 'access_token'})
print(activity_request.status_code)
pprint(activity_request.json()['activities-steps'])
 
