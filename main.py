from request.get import get
from request.get_id import get_id
from request.post1 import post1
from request.post2 import post2
from request.post3 import post3
from request.delete import delete
from request.feed import feed
from payloads.payload import payload_post
import os

# get Token from .env
auth_token = os.environ['TOKEN']

# Api-endpoint 
URL = "https://api.software.madkting.com/shops/1086093/products/"	

headers = {
	'Authorization': 'Token '+auth_token,
    'Content-Type': 'application/json'
    }

loading = "YGCwf02Oj96kzDM-9hcxKelZjiRk4IlJ"    
product_id = "21080059" #21080008
payload = { 'page': 4, 'page_size': 5 }

def get_products():
    get(URL, headers, payload)

def describe_product(product_id):
    get_id(URL, headers, product_id)

def add_product_1():
    post1(URL, headers)

def add_product_2():
    post2(URL, headers)

def add_product_3():
    post3(URL, headers, payload_post)        

def feed_state(loading):
    feed(headers, loading)

def delete_product(product_id):
    delete(URL, headers, product_id)