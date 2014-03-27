address_book = {}

def same_info(info):
    valid = False
    x = 0
    while valid == False:
        try:
            info = info + str(x)
            address_book[info]
            x += 1
            info = info[:-1]
        except KeyError:
            valid = True
    return info

y = 0
while True:
    info = str(input("Input a key: "))
    info = same_info(info)
    address_book[info] = y
    print(address_book)
    y += 1
    
