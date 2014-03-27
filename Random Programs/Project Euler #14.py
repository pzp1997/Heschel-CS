collatz = {}

for num in range(10):
    if num == 1:
        counter = 1
    else:
        counter = 2

    while not num == 1:
        if num%2 == 0:
            num = num/2
            counter += 1
        else:
            num = 3*num+1
            counter += 1

    collatz[counter] = num
    print(str(num) + ": " + str(counter))

key = list(collatz.keys())
key.sort()

print(collatz[key[0]])
