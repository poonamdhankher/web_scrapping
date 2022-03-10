from __future__ import print_function
from re import sub
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import csv
# open url
urlpage=urlopen("https://nutrabay.com/brand/optimum-nutrition-on/").read()
soup = BeautifulSoup(urlpage, "html.parser")
results= soup.find_all("div", {"class": "box-image"})
products = []
for result in results:
    imgTag= result.find("img")
    data = {}
    data['product_name'] = imgTag.get('alt')
    data['product_image'] = imgTag.get('src')
    products.append(data)

# dump json data
jsonstr= json.dumps(products)
with open('/Users/poonamdhankher/Downloads/test/scrapper_data/data.json', 'w') as f:
    print(jsonstr, file=f)
