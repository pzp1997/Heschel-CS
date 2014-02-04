#Product of Primes by Palmer Paul, 2013

#Finds the products of all the primes below (not inclusive of) the inputted integer

while True:
    usernum = str(input("Input a positive integer to return the product of all the primes below it: "))
    while usernum.isdigit() == False:
        print("You must input a positive integer.")
        usernum = str(input("Input a positive integer to return the product of all the primes below it: "))
    usernum = int(usernum)
    prime = [2]
    num = 3
    x = 0
    item = 1
    product = 2

    while usernum>num:
        if num%prime[x] != 0:
            if len(prime)>x+1:
                x = x + 1
            elif len(prime)<=x+1:
                prime.append(num)
                num = num + 1
                x = 0
        elif num%prime[x] == 0:
            num = num + 1
            x = 0

    while len(prime)>item:
        product = prime[item]*product
        item = item + 1
    
    print (product)
