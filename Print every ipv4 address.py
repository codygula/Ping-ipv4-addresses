# Print every ipv4 address

address1 = 0
address2 = 0
address3 = 0
address4 = 0

finalAddress = []

while address4 <= 255:
    while address3 <= 255:
        while address2 <= 255:
            while address1 <= 255:
                finalAddress = str(address1) + "." + str(address2) + "." + str(address3) + "." + str(address4)
                address1 = int(address1) + 1
                print(finalAddress)
            address2 += 1
            address1 = 0
        address3 += 1
        address2 = 0
    address4 += 1
    address3 = 0