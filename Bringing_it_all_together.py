#This wil import the Meraki Library
import meraki

#We import prettytable here to get a nice format for output
from prettytable import PrettyTable

#Insert your API key here
API_KEY = '<Insert API key>'

#This function is to get the org id of DevNet Sandbox
def getorgid(API_KEY):
    dashboard = meraki.DashboardAPI(API_KEY)
    response = dashboard.organizations.getOrganizations()
    for org in response:
        org_name = org['name']
        if org_name == 'DevNet Sandbox':
            org_id = org['id']
            return org_id

#This function is to get the network id of DevNet Sandbox ALWAYS ON
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

#We call the getorgid function and store the result in org_id
org_id = getorgid(API_KEY)

#We then call the get_net function using the org_id value we got in the previous step
get_net(org_id)
