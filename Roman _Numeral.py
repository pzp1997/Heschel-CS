## Roman_Numeral.py by Palmer Paul (March 5, 2014)

numerals_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
numerals_list = ["M", "CM", "D", "CD",  "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

print("Roman_Numeral.py by Palmer Paul (March 5, 2014)")
print("To quit at anytime, just input \"quit\" (without the quotation marks).")
print()

while True:
    num = input("Input a positive integer to see its Roman Numeral representation: ")
    while not num.isdigit() and not num.lower() == "q" and not num.lower() == "quit":
        if num.lower() == "quit" or num.lower() == "q":
            break
        else:
            print("You must input a positive integer.")
            num = input("Input a positive integer to see its Roman Numeral representation: ")
    num_orig = num
    num = int(num)

    if num > 4000 or num == 0:
        print("Error: this program can only handle positive integers less than 4000.")
    else:
        s = ""
        x = 0

        while num > 0:
            if num - numerals_dict[numerals_list[x]] >= 0:
                num -= numerals_dict[numerals_list[x]]
                s =  s + numerals_list[x]
                x = -1
            x += 1

        print(num_orig + ": " + s)
    print()
