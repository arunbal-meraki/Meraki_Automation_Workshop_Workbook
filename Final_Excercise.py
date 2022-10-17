#We import prettytable to print our results in nice format
from prettytable import PrettyTable

#We import the Meraki Library
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

#We call on the DashboardAPI function in the Meraki Library and pass it the API key
dashboard = meraki.DashboardAPI(API_KEY)

#We issue a GET request to get a list of orgs and store it in response
response = dashboard.organizations.getOrganizations()

#We then iterate through the list of orgs and search for the DevNet Sandbox org and store it's id in organization_id
for org in response:
    if org['name'] == 'DevNet Sandbox':
        organization_id = org['id']


#We then use the organization_id to get a list of devices in the org
response_devices = dashboard.organizations.getOrganizationDevicesAvailabilities(
    organization_id, total_pages='all')

#We then iterate through the list of devices and search for only wireless devices and then use prettytable to print the serial number and status.
t = PrettyTable()
t.field_names = ['Serial', 'Status']
for device in response_devices:
    if device['productType'] == 'wireless':
        t.add_row([device['serial'], device['status']])
print(t)
