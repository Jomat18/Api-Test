#!/usr/bin/env python

# importing librarys
import requests
import json 

payload = {
        "color": "negro",
        "price": 799,
        "sku": "L009K2HHM1",
        "stock": 10,
        "condition": "new",
        "size": "22.00",
        "part_number": "47200-220",
        "listing_type": "gold_special",
        "images": [
          {
            "url": "https://images-na.ssl-images-amazon.com/images/I/51C8Tg0TCaL._SX322_BO1,204,203,200_.jpg"
          },
          {
            "url": "https://images-na.ssl-images-amazon.com/images/I/51uLvJlKpNL._SX321_BO1,204,203,200_.jpg"
          },

        ],
        "name": "Book",
        "brand": "Amazon",
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

def post1(URL, headers):

  response = requests.request("POST", URL, headers=headers, data=parsed_data)

  if response.status_code != 201:
    raise ApiError('POST /products/ {}'.format(response.status_code))

  else:
    print(response.status_code) #201
    print (response.headers)