import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API key>"
}

response = requests.request('GET', url, headers=headers, data = payload)

r_json = response.json()

print(type(r_json))

print(r_json[0]['name'])


