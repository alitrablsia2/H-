dec=int(input("enter a decimal nimber: "))
pout=dec
bin=[]
while dec!=0:
    y=dec%2
    bin.append(y)
    dec=dec//2
bin.reverse()
print("the binary number of the "+str(pout)+" is: "+"".join([str(i) for i in bin]))