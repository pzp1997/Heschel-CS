def search_contact():
    found = []
    if len(contact_list_first) == 0 and len(contact_list_last) == 0:
        print("Address book is empty.")
        return False
    else:
        search = better_input("Search: ")
        search = search.lower()
        search_orig = search
        search = search.split()
        x = 0
        word = 0
        while True:
            if not search[word].isdigit():
                while search[word][-1].isdigit():
                    search = search[:-1]
                search = search + str(x)
            try:
                address_book[search]
                found.append(search)
                if search[word].isdigit():
                    search[word] = search[word] + "0"
            except KeyError:
                if search == "cancel" or search == "c":
                    return False
                elif x == 0 and not search.isdigit():
                    word += 1
                else:
                    return [search_orig, x-1]
            x += 1

        for x in range(len(found)):
            print(address_book[found[x]]["first_name"] + " \"" + address_book[found[x]]["nick"] + "\" " + address_book[found[x]]["last_name"])
            print("Phone: " + address_book[found[x]]["phone"])
            print("Email: " + address_book[found[x]]["email"])
            print()
