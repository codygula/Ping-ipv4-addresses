# This is a script I am making to ping every ipv4 address. So far, it will start at 0.0.0.0 and ping every IP address and print to the console.
# TODO: make it fill in a Hilbert Curve to create a map of the entire IPV4 internet.

import subprocess
import time

# ping -i sets interval between each ping, -c sets number of pings
def ping(ipaddress):
    out = subprocess.run("ping -c 1 " + ipaddress, capture_output=True, shell=True)
    return out
    

# create and open a new txt file
subprocess.run("cd /home", capture_output=True, shell=True)
document1 = subprocess.run("touch pingTest.txt", shell=True) # + time.strftime("%H:%M:%S") +".txt", shell=True)
print(document1)

e = open("pingTest.txt", "a")
e.write("######  ### #     #  #####  \n")
e.write("#     #  #  ##    # #     # \n")
e.write("#     #  #  # #   # #       \n")
e.write("######   #  #  #  # #  #### \n")
e.write("#        #  #   # # #     # \n")
e.write("#        #  #    ## #     # \n")
e.write("#       ### #     #  #####  \n \n")
e.write("Pinging IP addresses in range " + "0.0.0.0" + " to " + "255.255.255.255" + "\n")
e.write("Started at " + str(time.time()) +"\n")
e.write('\n')
e.close()


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
                z = ping(finalAddress)
                f = open("pingTest.txt", "a")
                f.write("######################################## ")
                f.write(z.stdout.decode())
                f.close()
                address1 = int(address1) + 1
            address2 += 1
            address1 = 0
        address3 += 1
        address2 = 0
    address4 += 1
    address3 = 0
print("done")