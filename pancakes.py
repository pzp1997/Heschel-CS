flour = str(input("How much flour do you have? "))
while str.isdigit(flour) == False:
    print("You must input an integer...")
    flour = str(input("How much flour do you have? "))
flour = int(flour)
flour = flour//3

milk = str(input("How much milk do you have? "))
while str.isdigit(milk) == False:
    print("You must input an integer...")
    milk = str(input("How much milk do you have? "))
milk = int(milk)
milk = milk//2

if flour>milk:
    flour = milk
if milk>flour:
    milk = flour
print("You can make", 7*(flour), "pancakes" + ".")
