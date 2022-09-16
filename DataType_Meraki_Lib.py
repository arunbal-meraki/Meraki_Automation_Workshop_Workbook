import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '<Insert API Key>'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)


response = dashboard.organizations.getOrganizations()

print(type(response))