from urllib3.exceptions import HTTPError
import urllib3
import requests


r = requests.get('https://in.ghn.vn/System/Report/PrintA5')
print(r.status_code)
