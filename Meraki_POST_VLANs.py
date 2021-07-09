import meraki
import pprint
import csv
import time
import variables

API_KEY = variables.KEY
NETWORK_MX12 = "L_676102894059004221"
NETWORK_MX34 = "L_676102894059004220"
dashboard = meraki.DashboardAPI(API_KEY)
api_call_counter = 0


def check_rate_limiting(counter):
    if counter == 5:
        time.sleep(1)
        counter = 0
    else:
        counter += 1
    return counter


# Read the CSV file with the list of VLANs to be added
with open('vlans_to_add.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        vlan_name = line[0]
        my_subnet = line[1]
        vlan_id = line[2]
        gateway = my_subnet.split('.0/24')[0] + '.254'
        reserved_ip_start = my_subnet.split('.0/24')[0] + '.1'
        reserved_ip_end = my_subnet.split('.0/24')[0] + '.20'

        # Create the VLAN
        api_call_counter = check_rate_limiting(api_call_counter)
        response = dashboard.appliance.createNetworkApplianceVlan(
            # NETWORK_MX12,
            NETWORK_MX34,
            vlan_id,
            vlan_name,
            subnet=my_subnet,
            applianceIp=gateway
        )

        pprint.pprint(response)

        # Update the DHCP attributes for the VLAN
        api_call_counter = check_rate_limiting(api_call_counter)
        response = dashboard.appliance.updateNetworkApplianceVlan(
            # NETWORK_MX12,
            NETWORK_MX34,
            vlan_id,
            reservedIpRanges=[{'start': reserved_ip_start, 'end': reserved_ip_end, 'comment': 'Reserved Range'}],
            dnsNameservers='google_dns'
        )

        pprint.pprint(response)

        print("\n###############################################################################################")
        print(f"Created VLAN: {vlan_id} | {vlan_name} | {my_subnet}")
        print("###############################################################################################\n")
