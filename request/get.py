#!/usr/bin/env python

# importing librarys
import requests
import json 
import os

# get Token from .env
#auth_token = os.environ['TOKEN']

# Api-endpoint 
URL = "https://api.software.madkting.com/shops/1086093/products/"	

headers = {
	'Authorization': 'Token 1b93d1275a169e1cfbfe04a394b8de793fa58f27',
    'Content-Type': 'application/json'
    }    

payload = { 'page': 4, 'page_size': 5 }


response = requests.get(URL, headers=headers, params=payload)

# extracting data in json format 
data = response.json() 

dictionary = json.dumps(data, sort_keys = True, indent = 4)
print(dictionary)