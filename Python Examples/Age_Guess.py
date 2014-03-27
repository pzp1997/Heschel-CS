#Guess Bill's Age by Palmer Paul, 2014

from random import randint

name = "Bill"
max_age = 120
age = randint(0, max_age)

while True:
    guess = input("Guess how old " + name + " is: ")
    while not guess.isdigit():
        print("Your guess must be a counting number.")
        guess = input("Guess how old " + name + " is: ")
    guess = int(guess)
    if guess>max_age:
        print(name + " is younger than " + max_age + " years old.")
    if guess>age:
        print(name + " isn't that old!")
    elif guess<age:
        print(name + " is older than that!")
    else:
        print("You win!")
        print()
        pa = input("Would you like to play again? ")
        while pa != "yes" and pa != "y" and pa != "no" and pa != "n":
            print("Please input \"yes\" or \"no\".")
            pa = input("Would you like to play again? ")
        if pa == "yes" or pa == "y":
            age = randint(0, max_age)
            print()
        else:
            raise SystemExit

