#GCF by Palmer Paul, 2013

#Input two integers to find their greatest common factor

while True:
    print ("Input two integers to return their Greatest Common Factor")
    num1 = int(input("Integer 1: "))
    num2 = int(input("Integer 2: "))
    factcheck = 1
    fact = []
    x = -1
    y = -2

    while factcheck<=num1:
        if num1%factcheck==0:
            fact.append(factcheck)
        factcheck = factcheck+1

    factcheck = 1

    while factcheck<=num2:
        if num2%factcheck==0:
            fact.append(factcheck)
        factcheck = factcheck+1

    list.sort(fact)

    while len(fact)>=abs(y):
        if fact[x] == fact [y]:
            break
        else:
            x = x - 1
            y = y - 1

    print (fact[x])
