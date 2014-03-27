for y in range(search_num + 1):
                if not search.isdigit():
                    while search[-1].isdigit():
                        search = search[:-1]
                search = search + str(y)
                try:
                    print(address_book[search]["first_name"] + " \"" + address_book[search]["nick"] + "\" " + address_book[search]["last_name"])
                    print("Phone: " + address_book[search]["phone"])
                    print("Email: " + address_book[search]["email"])
                    if search.isdigit():
                        search = search + "0"
                    if y != search_num:
                        print()
                except KeyError:
                    pass
            delete_contact()
