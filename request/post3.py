#!/usr/bin/env python

# importing librarys
import requests
import json 

def post3(URL, headers, payload_post):

    parsed_data = json.dumps(payload_post)

    response = requests.request("POST", URL, headers=headers, data=parsed_data)

    if response.status_code != 201:
        raise ApiError('POST /products/ {}'.format(response.status_code))

    else:
        print(response.status_code) #201
        print (response.headers)