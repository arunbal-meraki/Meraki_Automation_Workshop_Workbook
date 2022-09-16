#We import the requests library
import requests

#We store the API url in a variable
url = "https://api.meraki.com/api/v1/organizations"

#For a GET request the payload will be None
payload = None

#We set the headers and store in a variable
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}

#We issue a GET request using the url, headers and payload variables
response = requests.request('GET', url, headers=headers, data = payload)

#We check if the response is a 200 OK
if response.status_code == 200:
    print('Success!')
    print(response.text.encode('utf8'))
else:
    print('Oops! There was a problem!')


