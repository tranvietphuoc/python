import requests 
from requests.exceptions import HTTPError
import json


url = "https: // console.ghn.vn/api/v1/apiv3/OrderInfo"
json_in = {
    "token": "5d8ba90858515e3d6722fe06",
    "OrderCode": "EIKXK4A3Y"
    }

try:
    response = requests.get(url, json_in)

    # If response was successful, no Exception will be raised

    response.raise_for_status()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

response.encoding = 'utf-8'
response_heading = response.headers
response_content = response.text
response_json = response.json
print(response_heading)
print(response_content)
