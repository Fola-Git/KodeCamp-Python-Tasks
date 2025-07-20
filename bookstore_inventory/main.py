from inventory import add_book, list_books

while True:
    print("\n1. Add Book\n2. List Books\n3. Exit")
    choice = input("Choose: ")
    if choice == "1": add_book()
    elif choice == "2": list_books()
    else: break
