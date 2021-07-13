import meraki
import variables

API_KEY = variables.KEY
NETWORK_MX12 = "L_676102894059004221"
NETWORK_MX34 = "L_676102894059004220"
BASE_URL = "https://api.meraki.com/api/v1"
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

response = dashboard.appliance.getNetworkApplianceVlans(NETWORK_MX34)

for vlan in response:
    print('-----------------------------------------------------------------------------------------------')
    print(f'Name        : {vlan["name"]}')
    print(f'Subnet      : {vlan["subnet"]}')
    print(f'Gateway     : {vlan["applianceIp"]}')
    print(f'DHCP        : {vlan["dhcpHandling"]}, DNS: {vlan["dnsNameservers"]}')
    print(f'Reserved IPs: {vlan["reservedIpRanges"]}')
