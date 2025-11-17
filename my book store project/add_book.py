from save_all_books import save_all_books
def add_books(all_books):
    title = input("Enter book name: ")
    # while True:
    #     author = input("Enter author name by using semicolon (;) : ")
    #     if ',' in author:
    #         print("can't use comma (,)")
    #     else :
    #         break
    author = input("Enter author name: ")
    year = input("Enter the publishing year: ")
    price = float(input("Enter price: "))
    book = {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
    }

    all_books.append(book)
    save_all_books(all_books)
    print("book adding")
    return all_books