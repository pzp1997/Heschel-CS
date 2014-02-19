def engtomc():
    s = str(input("Input a word to convert it into International Morse Code: "))
    word = s.lower()
    mc = ""
    valid = True

    morsecode = {
        "a": "- ---",
        "b": "--- - - -",
        "c": "--- - --- -",
        "d": "--- - -",
        "e": "-",
        "f": "- - --- -",
        "g": "--- --- -",
        "h": "- - - -",
        "i": "- -",
        "j": "- --- --- ---",
        "k": "--- - ---",
        "l": "- --- - -",
        "m": "--- ---",
        "n": "--- -",
        "o": "--- --- ---",
        "p": "- --- --- -",
        "q": "--- --- - ---",
        "r": "- --- -",
        "s": "- - -",
        "t": "---",
        "u": "- - ---",
        "v": "- - - ---",
        "w": "- --- ---",
        "x": "--- - - ---",
        "y": "--- - --- ---",
        "z": "--- --- - -",
        "1": "- --- --- --- ---",
        "2": "- - --- --- ---",
        "3": "- - - --- ---",
        "4": "- - - - ---",
        "5": "- - - - -",
        "6": "--- - - - -",
        "7": "--- --- - - -",
        "8": "--- --- --- - -",
        "9": "--- --- --- --- -",
        "0": "--- --- --- --- ---",
        " ": "       "
        }

    if word == "!quit":
        quit()

    else:
        for letter in range(len(word)):
            try:
                mc = mc + morsecode[str(word[letter])] + "   "
            except KeyError:
                print("Invalid input: You may only input alphanumeric characters and spaces.")
                valid = False
                break

        if valid == True:
            print(s + ": " + mc)

print("Input !quit to exit the program.")
while True:
    engtomc()