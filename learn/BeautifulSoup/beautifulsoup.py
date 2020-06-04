import requests
from bs4 import BeautifulSoup
import csv
import re


r = requests.get('http://eloquentjavascript.net')

print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml')
print(soup.find_all('a'))

