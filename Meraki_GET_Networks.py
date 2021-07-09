import meraki
import variables

API_KEY = variables.KEY
dashboard = meraki.DashboardAPI(API_KEY)

org = dashboard.organizations.getOrganizations()[0]['id']

print('\n######################################################')
print(f'Organization ID: {org}')
print('######################################################\n')

networks = dashboard.organizations.getOrganizationNetworks(org)

for net in networks:
    print(f"{net['id']} | {net['name']}")
