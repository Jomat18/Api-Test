#!/usr/bin/env python

# importing librarys
import requests

def delete(URL, headers, product_id):
    URL = URL + product_id + "/"
    response = requests.delete(URL, headers=headers)

    print(response.status_code)
    print (response.headers)