import requests
import random
import string
from datetime import date, datetime, timedelta
for i in range(1,5):
    user_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    print('Testing with unexisting user: ' +user_name)
    # checking unexisting user
    r_get = requests.get('http://localhost:8080/hello/'+user_name)
    print ('got response code: '+str(r_get.status_code))
    if r_get.status_code != 400:
        raise('User already exists')
    birth_day = str(datetime.today().date())
    print('Now lets add this user that has birhtday today ... '+birth_day)
    r_put = requests.put('http://localhost:8080/hello/'+user_name, json= {'dateOfBirth':birth_day})
    print ('got response code: '+str(r_put.status_code))
    print('Check if user exists now ...')
    r_get = requests.get('http://localhost:8080/hello/'+user_name)
    print ('got response code: '+str(r_get.status_code))
    if r_get.status_code != 200:
        raise('User doesnt exists')
    print('Checking for happy birhday message')
    if 'Happy Birthday' not in  r_get.json()['message']:
        raise('wasnt happy birthday' )
    print('Done ...')
    print('Will update birthday to 10   days before today')
    birth_day =  str((datetime.today() - timedelta(days=10)).date())
    r_put = requests.put('http://localhost:8080/hello/'+user_name, json= {'dateOfBirth':birth_day})
    print ('got response code: '+str(r_put.status_code))
    print('Check if user date changed')
    r_get = requests.get('http://localhost:8080/hello/'+user_name)
    print ('got response code: '+str(r_get.status_code))
    if r_get.status_code != 200:
        raise('User doesnt exists')
    print(r_get.json()['message'])
    print('Checking for happy birhday message')
    if 'Your birthday was 10 days ago' not in  r_get.json()['message']:
        raise('wasnt 10 days agot' )
