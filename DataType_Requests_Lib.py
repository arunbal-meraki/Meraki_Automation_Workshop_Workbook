import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}

response = requests.request('GET', url, headers=headers, data = payload)

#print(response.text.encode('utf8'))

print(type(response))
