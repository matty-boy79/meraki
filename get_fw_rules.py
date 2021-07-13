import meraki
import variables
import pprint

API_KEY = variables.KEY
NETWORK_MX12 = "L_676102894059004221"
NETWORK_MX34 = "L_676102894059004220"
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

response = dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(
    NETWORK_MX12
)

pprint.pprint(response)
