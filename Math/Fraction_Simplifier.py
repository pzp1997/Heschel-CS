## Fraction_Simplifier.py by pzp1997 (March 9, 2014)
## Written in Python 3.3.4

print("Fraction_Simplifier.py by pzp1997 (March 9, 2014)")
print("To quit at anytime, just input \"quit\".")
print()

while True:
    foo = input("Input a fraction to simplify it: ")
    if foo.lower() == "quit" or foo.lower() == "q":
        break
        print("The program has been stopped.")
    slashindex = foo.find("/")
    while not foo[0:slashindex].isdigit() or not foo[slashindex+1:].isdigit() or not "/" in foo:
        print("Input the fraction in the format \"num1/num2\" (don't forget the \"/\").")
        foo = input("Input a fraction to simplify it: ")
        if foo.lower() == "quit" or foo.lower() == "q":
            raise SystemExit
        slashindex = foo.find("/")
    num1 = int(foo[0:slashindex])
    num2 = int(foo[slashindex+1:])
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
        if fact[x] == fact[y]:
            break
        else:
            x = x - 1
            y = y - 1

    print(str(num1/fact[x])[:-2] + "/" + str(num2/fact[x])[:-2])
