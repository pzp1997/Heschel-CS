#Prime Number Generator by Palmer Paul, 2013

while True:
    usernum = int(input("Input an integer to return all the primes below it: "))
    prime = [2]
    num = 3
    x = 0

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

    print (prime)
    print()
