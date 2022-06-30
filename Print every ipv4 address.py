# 
#
# TODO fix the ending range. It will not stop at the inputed end point becasue it is always less than 
# or equal to 255. Right now it can start pinging from any IPV4 address and keep going upward. 
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
    return address1, address2, address3, address4, ip

# This takes input, but does not work.
def splitEndingIP():
    print("Ending IP: ")
    endip = input()
    endiparray = endip.split(".")
    endaddress4 = int(endiparray[0])
    endaddress3 = int(endiparray[1])
    endaddress2 = int(endiparray[2])
    endaddress1 = int(endiparray[3])
    return endaddress1, endaddress2, endaddress3, endaddress4, endip


address1, address2, address3, address4, ip = splitStartingIP()
endaddress1, endaddress2, endaddress3, endaddress4, endip = splitEndingIP()
preamble(ip, endip)

finalAddress = []

# This does not work. It will never stop at the desired end point because 255 will always be equal or higher.
# This whole thing may need to be refactored. It will start at any desired address, it just won't stop at one.
while address4 <= max(endaddress4, 255):
    while address3 <= max(endaddress3, 255):
        while address2 <= max(endaddress2, 255):
            while address1 <= max(endaddress1, 255):
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