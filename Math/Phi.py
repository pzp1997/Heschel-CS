#Phi by Palmer Paul, 2013

#Approximates Phi (aka The Golden Ratio)

x = 1
y = 1
z = 1
while x<100000000:
    z=x
    x=y
    y=z+x
    print (y/x)
