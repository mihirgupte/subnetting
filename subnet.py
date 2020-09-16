import math

ipa = input("Enter the block given: ")
add = ipa.split("/")
bits = int(add[1])
ip = add[0].split(".")
subnet = int(input("Enter the no. of subnets: "))

def check(add):
    if len(add)!=2:
        print("Enter a valid block with bits allocated to a network for eg. 192.25.78.25/28\n")
        return False
    ip = add[0].split(".")
    if len(ip)!=4:
        print("enter a valid ip address")
        return False
    for i in ip:
        if int(i)>255:
            print("Enter a valid ip address with 255 range")
            return False
    return True

def n2b(ip):
    ipb=[]
    x=""
    for i in range(len(ip)):
        x="{0:b}".format(int(ip[i]))
        x = x+ "0"*(8-len(x))
        ipb.append(x)
    return ipb

def bTd(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal 

def subnet_creation(subnet,ipb,bits):
    amt = math.ceil(math.log2(subnet))
    if 32-bits<amt:
        print("cannot have these many subnets on the given network right now")
        return False
    subnet_mask=[]
    for i in range(len(ipb)):
        if i==3:
            s = "1"*(amt) + "0"*(8-amt)
            subnet_mask.append(s)
            break
        subnet_mask.append("1"*8)
    mask = ""
    for i in subnet_mask:
        mask = mask + str(bTd(int(i))) + "."
    return [mask[:len(mask)-1],amt]

mask,amt = subnet_creation(subnet, n2b(ip),bits)
print("the subnet mask is:", mask)
addr = pow(2, (8 - amt))
print("the no. of addresses in each subnet is:" , addr,"\n")

def all_addr(ip,amt,addr):
    ip3=0
    for i in range(pow(2,amt)):
        ip[3] = str(ip3)
        print("the address for the",i+1, "subnet is:\n")
        add = ".".join(ip)
        print("the first address is ", add)
        ip3 = ip3+addr-1
        ip[3] =  str(ip3)
        add = ".".join(ip)
        print("the last address is ", add,"\n")
        ip3= ip3+1

all_addr(ip, amt, addr)