import os
from os.path import join, getsize
import requests
import json

def sendToDjango(drink_type, drink):
    url = "http://localhost:8000/brewery/drink/add/"
    query = {"drink_type": drink_type, "drink": drink}
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(
            url=url, data=json.dumps(query), headers=headers, timeout=5)
        response = json.loads(response.content)
        print("posted %s: %s"%(drink, response))
    except Exception as e:
        print("Exception: %s"%e)


for root, dirs, files in os.walk('.'):
    if os.path.isdir(root) and root!='.':
        print(root)
        print('*'*len(root))
        print('\n')
        for name in files:
            print(name)
            sendToDjango(root[2:], name.split('.')[0])
        print('\n\n')