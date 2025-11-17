from save_all_books import save_all_books
def delete_book (all_books):
    search_result = False
    search_item = input("Enter title or author's for name delete book")
    matching_book = []
    for index, book in enumerate(all_books):
        if (search_item.lower() in book ["title"].lower() or search_item.lower() in book ["author"].lower())
            search_result = True
            matching_book.append((index, book))


            print(f"{len(matching_book)}.title: {book['title']} - author: {book['author']}")
            if not search_result