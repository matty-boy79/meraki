import meraki
import meraki_v0
import variables

API_KEY = variables.KEY
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)
dashboard_v0 = meraki_v0.DashboardAPI(API_KEY, suppress_logging=True)

org = dashboard.organizations.getOrganizations()[0]['id']
print(f'\nOrganization ID: {org}\n')

networks = dashboard.organizations.getOrganizationNetworks(org)

for net in networks:
    net_id = net['id']
    net_name = net['name']

    print("\n===================================================================")
    print(f"{net_id} - {net_name}")
    print("===================================================================")

    devices = dashboard_v0.devices.getNetworkDevices(net_id)
    for device in devices:
        if 'name' in device.keys():
            print(f"{device['serial']} = {device['name']}")
