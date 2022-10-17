# Welcome to the Meraki Automation Workshop!

This repository contains scripts which will be used during the demo's and the Final Excercise.

---

## Prepare for the Workshop

- Have Python already installed on your local machine or use a Linux VM
- If you don't have Python use [PythonAnywhere](https://www.pythonanywhere.com)
    - If using pythonanywhere upload the python files to the directory there and run the scripts from there.
- Optional, install ipython using pip
```bash
pip install ipython
```
---

## Instructions on using the code during the workshop

- Use the API key provided in [API docs](https://developer.cisco.com/meraki/api-v1/#!get-organizations)
- Copy paste the code to ipython or python interpreter
- Use an editor such as Visual Studio Code
    - create a python file and copy the code 
    - Save as .py file.
    - Run the file in terminal or within the editor.

---

## Python Virtual Environment

- This is to be run in *bash* shell

```bash
python -m venv workshop
cd workshop
source ./bin/activate
```

- To deactivate the venv

```bash
deactivate
```

## Meraki Python Library Demo

- Install the *meraki library* using *pip*.

```bash
pip install meraki
```
Run a GET request using meraki library for a list of organizations.

```python
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)


response = dashboard.organizations.getOrganizations()

print(response)
```
---

## Requests Python Library Demo

- If *requests* not already installed, install it using *pip*.

```bash
pip install requests
```

Run a GET request using the requests library

```python
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```
---

## Data Types Demo

- Here we use *meraki library* GET request code and print the type of response to check the response data type
```python
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.organizations.getOrganizations()

print(type(response))
```
- Copy the requests library GET request code from below to check the response data type
```python
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}
response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

print(type(response))
```

---

## For and While Loops Demo

- Using a *for* loop to process the *response*.

```python
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/
dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.organizations.getOrganizations()

for org in response:
    print(org['name'], "->", org['id'])
```
- Using a *while* loop to print the first 10 orgs

```python
while n <= 9:
    print('Org->', n, response[n])
    print('--------------------------')
    n = n + 1
```
---

## If..else Demo 1

- Using *if..else* statements we get the org ID of *DevNet Sandbox*.

```python
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/
dashboard = meraki.DashboardAPI(API_KEY)

response = dashboard.organizations.getOrganizations()

for org in response:
    if org['name'] == 'DevNet Sandbox':
        print('DevNet Sandbox Found!')
        print(org['id'])
```
Here we will use if..else to verify the response.

```python
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}
response = requests.request('GET', url, headers=headers, data = payload)

if response.status_code == 200:
    print('Success!')
    print(response.text.encode('utf8'))
else:
    print('Oops! There was a problem!')   
```

## If..else Demo 2

- Here we will use *if..else* to check the *response*.

```python
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}

response = requests.request('GET', url, headers=headers, data = payload)

if response.status_code == 200:
    print('Success!')
    print(response.text.encode('utf8'))
else:
    print('Oops! There was a problem!')
```

---

## JSON with Python Demo

- Here we use *json()* function to convert the *response* to *list* data type.

```python
import requests

url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "<Insert API Key>"
}

response = requests.request('GET', url, headers=headers, data = payload)

r_json = response.json()

print(type(r_json))

for org in r_json:
    print(org)
```
---

## Bringing it All Together Demo

- Install prettytable

```bash
pip install prettytable
```
- Here use functions to get the network ID of *DevNet Sandbox ALWAYS ON*.

```python
import meraki

from prettytable import PrettyTable

API_KEY = '<Insert API Key>'

def getorgid(API_KEY):
    dashboard = meraki.DashboardAPI(API_KEY)
    response = dashboard.organizations.getOrganizations()
    for org in response:
        org_name = org['name']
        if org_name == 'DevNet Sandbox':
            org_id = org['id']
            return org_id

def get_net(org_id):
    dashboard = meraki.DashboardAPI(API_KEY)
    organization_id = org_id
    response = dashboard.organizations.getOrganizationNetworks(
                organization_id, total_pages='all')
    for net in response:
        if net['name'] == 'DevNet Sandbox ALWAYS ON':
            t = PrettyTable(['Network Name', 'Network ID'])
            t.add_row([net['name'], net['id']])
            print(t)

org_id = getorgid(API_KEY)

get_net(org_id)
```
---

## Reading from a CSV file Demo

- This code reads from an inventory *CSV* file and gets the serial numbers and stores them in a list called *serials*.

```python
import csv

serials =[]

with open('<Insert name of CSV file>') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        if line_count == 1:
            serials.append(row["serial_number"])
            
print(serials)
```
---

## Final Exercise

List the status of wireless AP's in the *DevNet Sandbox* org.

1. Go to [Meraki API Docs](https://developer.cisco.com/meraki/api-v1) Navigate to the [GET organizations request](https://developer.cisco.com/meraki/api-v1/#!get-organization)
2. Under Template copy the Meraki Library code snippet
3. Use your favourite editor or ipython
4. Paste it into your editor.
5. Make sure to *import meraki*.
```python
import meraki
```
6. Import prettytable as well, as we will use a table to print out the status of AP's.
```python
from prettytable import PrettyTable
```
7. Remove the *print(response)* statement
8. Copy the following code and append it to the previous code.
```python
for org in response:
    if org['name'] == 'DevNet Sandbox':
        organization_id = org['id']
```
9. Navigate to [GET organizations devices Availability](https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities)
10. Copy the following line append it the previous code.
```python
response_devices = dashboard.organizations.getOrganizationDevicesAvailabilities(
    organization_id, total_pages='all')
```
11. Copy the following code snippet and append it to the code as well.
```python
for device in response_devices:
    if device['productType'] == 'wireless':
        t = PrettyTable()
        t.field_names = ['Serial', 'Status']
        t.add_row([device['serial'], device['status']])
        print(t)
```
12. If you are using an editor make sure to save the file as a python file (use .py extension)
13. Run the file or if you are using ipython just hit Enter.
14. You will now see an output of the status of wireless AP's with their serial number.

