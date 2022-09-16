#We import the Meraki Library
import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

#We call on the DashboardAPI function and pass it the API key
dashboard = meraki.DashboardAPI(API_KEY)

#We do a GET request to get a list of orgs and then store the result in response
response = dashboard.organizations.getOrganizations()

#We then iterate through the list of orgs and print the name and id.
for org in response:
    print(org['name'], "->", org['id'])