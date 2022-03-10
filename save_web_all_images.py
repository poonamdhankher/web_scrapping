import requests
from bs4 import BeautifulSoup

url ="https://nutrabay.com/"

#send get request
response = requests.get(url)

html_page = BeautifulSoup(response.text, 'html.parser')

images = html_page.find_all("img")

for index, image in enumerate(images):
    image_url= image.get("src")      #img src value
    
    image_extension= image_url.split(".")[-1]       #get image extension

    #get image data
    image_bytes = requests.get(image_url).content


    
    if image_bytes:
        #write the image data
        with open(f"Image {index+1}.{image_extension}", "wb") as file:
            file.write(image_bytes)
            print(f"Downloading image {index+1}.{image_extension}")



'''from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://nutrabay.com/')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')'''
