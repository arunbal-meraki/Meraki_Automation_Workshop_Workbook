#We import the Meraki Library
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

#We call on the DashboardAPI function and pass it the API key
dashboard = meraki.DashboardAPI(API_KEY)

#We issue a GET request and store the list.
response = dashboard.organizations.getOrganizations()

#We use a for loop to iterate through the list of orgs and the if the org name is DevNet Sandbox then we print the id.
for org in response:
    if org['name'] == 'DevNet Sandbox':
        print('DevNet Sandbox Found!')
        print(org['id'])
        