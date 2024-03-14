import requests;
from bs4 import BeautifulSoup;

url="write the url of website"
r=requests.get(url)
print(r.text)