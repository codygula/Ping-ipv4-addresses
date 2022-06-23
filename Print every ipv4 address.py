# Ping every ipv4 address

import subprocess

# ping -i sets interval between each ping, -c sets number of pings
def ping(ipaddress):
    out = subprocess.run("ping -c 1 " + ipaddress, shell=True)
    return out
    
address1 = 0
address2 = 0
address3 = 0
address4 = 0

finalAddress = []

while address4 <= 255:
    while address3 <= 255:
        while address2 <= 255:
            while address1 <= 255:
                finalAddress = str(address4) + "." + str(address3) + "." + str(address2) + "." + str(address1)
                print("now pinging " + finalAddress)
                print(ping(finalAddress))
                address1 = int(address1) + 1
            address2 += 1
            address1 = 0
        address3 += 1
        address2 = 0
    address4 += 1
    address3 = 0
print("done")