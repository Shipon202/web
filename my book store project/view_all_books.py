def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"title:{book['title']} | author:{book['author']} | year:{book['year']}")
        else:
            print("No in there")