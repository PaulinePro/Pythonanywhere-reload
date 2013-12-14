#!/usr/bin/python

import requests

USERNAME = ''
PASSWORD = ''
reload_url = 'https://www.pythonanywhere.com/user/%s/webapps/%s.pythonanywhere.com/reload' % (USERNAME, USERNAME) 
login_url = 'https://www.pythonanywhere.com/login/'

headers = {'Referer': 'https://www.pythonanywhere.com/login/?next=/',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
           'Host': 'www.pythonanywhere.com',
           'Origin': 'https://www.pythonanywhere.com'}
session = requests.session()
session.headers.update(headers)

# GET the csrf token
response = session.get(login_url)
if response is not None:
    csrf_token = response.cookies['csrftoken']
    if csrf_token is not None:
        # Login with payloads
        data = {'csrfmiddlewaretoken': csrf_token,
                'username': USERNAME,
                'password': PASSWORD,
                'next': '/'}
        session.post(login_url, data=data)
        
        # Reload the web app
        response = session.post(reload_url)
        if response.status_code == 200:
            print 'Reload successful'
        else:
            print 'Reload failed'
