from __future__ import print_function
from re import sub
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import cv2
import requests

# import json data
with open('/Users/poonamdhankher/Downloads/test/scrapper_data/data.json', 'r') as products:
    products = json.load(products)

 
# save images
for product in products:
    product_name = product['product_name']
    product_image = product['product_image']
    if(product_name == None or product_image == None):
        continue   
    f = open('/Users/poonamdhankher/Downloads/test/scrapper_data/' + product_name + '.jpg','wb')
    response = requests.get(product_image)
    f.write(response.content)
    f.close()
print("download successful")