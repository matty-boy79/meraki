Create a file called variables.py and add one variable called KEY with your Meraki console API key as the string value, like this:

KEY = "abcdef0123456789fedcba9876543210!

To create VLANs, update the vlans_to_add.txt file with a CSV list of the VLANs to add
The first value is the VLAN name, the second is the subnet and the third is the VLAN number
The script will set the default gateway to x.x.x.254
The script will change the DHCP scope to use google DNS and reserve the first 20 IPs
Note - The script only works for /24 subnets as I coulnd't be arsed making it work for anything! I probably will at some point.

<p>MyVlanName,10.15.15.0/24,15</p>
<p>MyOtherVlanName,10.16.16.0/24,16</p>
