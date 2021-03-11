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

payload = {
        "color": "negro",
        "price": 5999.98,
        "sku": "B1234567",
        "stock": 50,
        "condition": "new",
        "size": "22.00",
        "part_number": "47200-220",
        "listing_type": "gold_special",
        "images": [
          {
            "url": "https://icdn5.digitaltrends.com/image/digitaltrends_es/new-macbook-pro-closing-2-640x640.jpg"
          },
          {
            "url": "https://parentesis.com/imagesPosts/Newmac2018_int.jpg"
          },
          {
            "url": "https://actualidadinformativa.com.do/wp-content/uploads/2020/11/air2-1.jpg"
          },
          {
            "url": "https://i.pinimg.com/originals/1e/d0/b3/1ed0b37a7a2c3cda8fa3e83e4932e199.jpg"
          },
        ],
        "name": "Laptop",
        "brand": "Apple",
        "depth": 21,
        "description": "Plataforma Abierta Para Mujer Rafael Ferrigno 2704-047200 Color Negro En Acabado Sillero",
        "dimensions_unit": "cm",
        "height": 11,
        "gender": "female",
        "shipping_depth": 21,
        "shipping_height": 11,
        "shipping_price": 0,
        "shipping_width": 31,
        "shipping": 0,
        "sku_simple": "047200",
        "weight": 0.8,
        "weight_unit": "kg",
        "tax": "16",
        "width": 31,
        "description_html": "<strong>Plataforma para Mujer Rafael Ferrigno 2704-047200 Color Negro</strong>",
        "template_html": "default_plain_text",
        "model": "47200-220-047200",
        "category_pk": 559
}

parsed_data = json.dumps(payload)

response = requests.request("POST", URL, headers=headers, data=parsed_data)

print(response.status_code) #201
print (response.headers)