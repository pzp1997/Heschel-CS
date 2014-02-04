userinput = str(input("Input a positive integer to list the pairs of numbers below and equal to it, whose squares have the same last two digits: "))

while str.isdigit(userinput) == False:
    userinput = str(input("You must input a positive integer: "))
userinput = int(userinput)

for num in range (200, userinput+1):
    x = 4
    y = 4
    pairs = []
    print(num)
    while y<=num:
        if str(x**2)[-1] == str(y**2)[-1] and str(x**2)[-2] == str(y**2)[-2] and x != y:
            pairs.append(x+y)
            x += 1
            if x>num:
                x = y
                y += 1
        else:
            x += 1
            if x>num:
                x = y
                y += 1
    
    print("Number of pairs: " + str(len(pairs)))
    print()
