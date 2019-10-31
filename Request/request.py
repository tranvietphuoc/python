import requests
from requests.exceptions import HTTPError
import json
import csv

url = 'https://console.ghn.vn/api/v1/apiv3/OrderInfo'
# url = 'https://dev-online-gateway.ghn.vn/apiv3-api/api/v1/apiv3/OrderInfo'
data = {
    "token": "5db938e7113d124b11772692",
    "OrderCode": "EJAQ3YSN7"
    }

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }


try:
    r = requests.post(url, data=json.dumps(data), headers=headers)

    # If response was successful, no Exception will be raised

    r.raise_for_status()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

# response.encoding = 'utf-8'

# with open('data.csv', 'w') as f:
#     csv_writer = csv.writer(f, delemiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for content in r.text:
#         csv_writer.writerow(r.text)
print(r.url)
print(r.text)
