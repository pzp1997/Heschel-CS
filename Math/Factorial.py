num = int(input("Input a number to return its factorial: "))
product = num

while num>1:
    num = num - 1
    product = product*(num)

print (product)
