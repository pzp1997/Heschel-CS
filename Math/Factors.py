num = int(input("Input an integer to return its factors: "))
factcheck = 1
fact = []

while factcheck<=num:
    if num%factcheck==0:
        fact.append(factcheck)
    factcheck = factcheck+1

print (fact)
