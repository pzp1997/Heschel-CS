#Scrabble Score (version 1.0) by Palmer Paul, 2/2/2014

s = str(input("Input a word to get its Scrabble score: "))
while s.isalpha() == False:
    print("Your word must only contain letters.")
    s = str(input("Input a word to get its Scrabble score: "))
word = s.lower()
score = 0
values = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
    }

for letter in range(len(word)-1):
    score += values[str(word[letter])]

print(str(s) + ": " + str(score))
