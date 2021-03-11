#!/usr/bin/env python

# importing librarys
import requests
import json 
import os

# get Token from .env
#auth_token = os.environ['TOKEN']

# Api-endpoint 
URL = "https://api.software.madkting.com/shops/1086093/products/21080059/"

headers = {
	'Authorization': 'Token 1b93d1275a169e1cfbfe04a394b8de793fa58f27',
    }    

response = requests.delete(URL, headers=headers)

print(response.status_code)
print (response.headers)