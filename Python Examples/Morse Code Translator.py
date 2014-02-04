def engtomc():
    s = str(input("Input a word to convert it into International Morse Code: "))
    word = s
    word.replace(" ", "")
    print(word)
    while s.isalnum() == False:
        print("You may only input alphanumeric characters.")
        s = str(input("Input a word to convert it into International Morse Code: "))
    word = s.lower()
    mc = ""

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

    for letter in range(len(word)):
        mc = mc + morsecode[str(word[letter])] + "   "

    print(s + ": " + mc)

while True:
    engtomc()
