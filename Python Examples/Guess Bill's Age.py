#Guess Bill's Age by Palmer Paul, 2014

from random import randint

name = "Bill"
max_age = 120
age = randint(0, max_age)

def game():
    guess = str(input("Guess how old " + name + " is: "))
    while guess.isdigit() == False:
        print("Your guess must be a counting number.")
        guess = str(input("Guess how old " + name + " is: "))
    guess = int(guess)
    if guess>120:
        print(name + " is younger than " + max_age + " years old.")
        game()
    if guess>age:
        print(name + " isn't that old!")
        game()
    elif guess<age:
        print(name + " is older than that!")
        game()
    elif guess == age:
        print("You win!")
        playagain()

def playagain():
    print()
    pa = str(input("Would you like to play again? "))
    while pa != "yes" and pa != "y" and pa != "no" and pa != "n":
        print("Please input \"yes\" or \"no\".")
        pa = str(input("Would you like to play again? "))
    if pa == "yes" or pa == "y":
        age = randint(0, 120)
        print()
        game()
    elif pa == "no" or pa == "n":
        pass

game()
