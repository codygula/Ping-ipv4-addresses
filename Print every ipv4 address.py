# 
#
# TODO Make it work for any IP range. It currently seems to work for ranges that make sense, 10.0.0.1 - 10.0.0.10 etc.,
# but not for ranges like 5.6.7.8 - 6.7.8.9. The nexted while loops need to be replaced.
# TODO make it fill in a Hilbert Curve to create a map of the entire IPV4 internet.

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

def preamble(beginingIP, endIP):
    e = open("pingTest.txt", "a")
    e.write("######  ### #     #  #####  \n")
    e.write("#     #  #  ##    # #     # \n")
    e.write("#     #  #  # #   # #       \n")
    e.write("######   #  #  #  # #  #### \n")
    e.write("#        #  #   # # #     # \n")
    e.write("#        #  #    ## #     # \n")
    e.write("#       ### #     #  #####  \n \n")
    e.write("Pinging IP addresses in range " + beginingIP + " to " + endIP + "\n")
    e.write("Started at " + str(time.strftime('%Y-%m-%d %H:%M:%S') +"\n"))
    e.write('\n')
    e.close()


def splitStartingIP():
    print("Starting IP: ")
    ip = input()
    iparray = ip.split(".")
    address4 = int(iparray[0])
    address3 = int(iparray[1])
    address2 = int(iparray[2])
    address1 = int(iparray[3])
    if address4 > 255 or address4 < 0:
        print("error")
    if address3 > 255 or address4 < 0:
        print("error")
    if address2 > 255 or address4 < 0:
        print("error")
    if address1 > 255 or address4 < 0:
        print("error")
    return address1, address2, address3, address4, ip


def splitEndingIP():
    print("Ending IP: ")
    endip = input()
    endiparray = endip.split(".")
    endaddress4 = int(endiparray[0])
    endaddress3 = int(endiparray[1])
    endaddress2 = int(endiparray[2])
    endaddress1 = int(endiparray[3])
    if address4 > 255 or address4 < 0:
        print("error")
    if address3 > 255 or address4 < 0:
        print("error")
    if address2 > 255 or address4 < 0:
        print("error")
    if address1 > 255 or address4 < 0:
        print("error")
    return endaddress1, endaddress2, endaddress3, endaddress4, endip


address1, address2, address3, address4, ip = splitStartingIP()
endaddress1, endaddress2, endaddress3, endaddress4, endip = splitEndingIP()
preamble(ip, endip)

finalAddress = []

# This still does not work correctly.
while address4 <= endaddress4:
    while address3 <= endaddress3:
        while address2 <= endaddress2:
            while address1 <= endaddress1:
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
f = open("pingTest.txt", "a")
f.write("Ended at " + str(time.strftime('%Y-%m-%d %H:%M:%S') +"\n"))
f.close()
print("done")