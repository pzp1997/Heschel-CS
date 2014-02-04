#Quadratic Roots by Palmer Paul, 2013

#Uses quadratic formula to solve for the variable

##bugs
#if input is not an integer, the program will crash

while True:
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    roots = [(-b + (b**2-4*a*c)**0.5)/(2*a), (-b - (b**2-4*a*c)**0.5)/(2*a)]
    roots.sort(key=int)

    print (roots)
