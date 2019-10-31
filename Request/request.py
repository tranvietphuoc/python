import requests
from requests.exceptions import HTTPError
import json
import csv
# from flask import Flask


# Get data from GHN's api, then save to csv file

url = 'https://console.ghn.vn/api/v1/apiv3/OrderInfo'
# url = 'https://dev-online-gateway.ghn.vn/apiv3-api/api/v1/apiv3/OrderInfo'

OrderCodes = ["EJR7X6AXS", "EJY6X7D9A", "EJ5DQFFUL", "EJDQF6RFA", "EJSHH6HD9"]
token = "5d8ba90858515e3d6722fe06"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    }


results = list()  # contain all of contents are responsed
for ordercode in OrderCodes:
    data = dict()  # make a dict to hold query data
    data.update({'token': token})
    data.update({'OrderCode': ordercode})
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
        results.append(json.loads(r.text)['data'])

with open('data.csv', 'w') as file:
    csv_writer = csv.writer(file, delimeter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['OrderCode', 'OrderStatus', 'ToDistrict', 'SortCode'])
    for result in results:
        csv_writer.writerow(result['OrderCode'],result['CurrentStatus'], )
