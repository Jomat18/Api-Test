#!/usr/bin/env python

# importing librarys
import requests
import json 
import os
from payloads.payload import payload

# get Token from .env
#auth_token = os.environ['TOKEN']

# Api-endpoint 
URL = "https://api.software.madkting.com/shops/1086093/products/"	

headers = {
	'Authorization': 'Token 1b93d1275a169e1cfbfe04a394b8de793fa58f27',
    'Content-Type': 'application/json'
    }    

parsed_data = json.dumps(payload)

response = requests.request("POST", URL, headers=headers, data=parsed_data)

print(response.status_code) #201
print (response.headers)