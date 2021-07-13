import meraki
import variables

API_KEY = variables.KEY
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

org = dashboard.organizations.getOrganizations()[0]['id']

print(f'\nOrganization ID: {org}\n')

networks = dashboard.organizations.getOrganizationNetworks(org)

for net in networks:
    print(f"{net['id']} = {net['name']}")
