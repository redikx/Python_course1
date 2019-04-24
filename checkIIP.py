ipAddress = input("Enter IP addres : ")
#ipAddress="123.456.789.000"
print("Address to check {0}".format(ipAddress))

fulladdress = []
field = 0
addr=''
for char in ipAddress:
    if char in '1234567890':
        addr+=char
    else:
        if char == '.':
            fulladdress.append(addr)
            addr=''
            continue
        else:
            print("Wrong character!")
            exit(99)

# check for last sign "."
if len(addr) > 0 :
    fulladdress.append(int(addr))
    print(fulladdress)

# Check format xxx.xxx.xxx.xxx
if len(fulladdress) > 4:
    print("Two many values in address")
    exit(10)
if len(fulladdress) < 4:
    print("Two little values in address")
    exit(10)
i=0

for saddr in (fulladdress):
    if  int(saddr) < 0 or int(saddr) > 255:
        print("Address {0} out of scope ({1})"
              .format(int(i+1),saddr))
    i=i+1




