#!/usr/bin/env python

# importing librarys
import requests
import json 

def get_id(URL, headers, product_id):
    URL = URL + product_id + "/"
    response = requests.get(URL, headers=headers)

    # extracting data in json format 
    data = response.json() 

    dictionary = json.dumps(data, sort_keys = True, indent = 4)
    print(dictionary)