#!/usr/bin/env python

# importing librarys
import requests
import json 

def feed(headers, loading):
    URL = "http://api.software.madkting.com/feeds/"+ loading +"/"

    response = requests.get(URL, headers=headers)

    # extracting data in json format 
    data = response.json() 

    dictionary = json.dumps(data, sort_keys = True, indent = 4)
    print(dictionary)