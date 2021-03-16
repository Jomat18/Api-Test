#!/usr/bin/env python

# importing librarys
import requests
import json 


def get(URL, headers, payload):
    response = requests.get(URL, headers=headers, params=payload)

    if response.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /products/ {}'.format(response.status_code))

    else:
        # extracting data in json format 
        data = response.json() 

        dictionary = json.dumps(data, sort_keys = True, indent = 4)
        print(dictionary)
    