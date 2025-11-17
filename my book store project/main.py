import add_book
import view_all_books
import delete_book

all_books = []
print("Wellcome to book store")
manu_text = """
please select option :
0.exit
1. add book
2. view all book 
3. delete book 
"""

while True:
    print(manu_text)
    menu = input("Input a number : ")
    if menu == "0":
        break
    elif menu == "1":
        all_books == add_book.add_books(all_books)
    elif menu == "2":
       view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books == delete_book.delete_book(all_books)
    else:
        print("Invalid input")

