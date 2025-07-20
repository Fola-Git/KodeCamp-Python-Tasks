import json, os, math

DATA_FILE = "books.json"

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = round(price, 2)
        self.stock = stock

def load_books():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_books(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_book():
    title = input("Book Title: ")
    author = input("Author: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    book = Book(title, author, price, stock)
    books = load_books()
    books.append(book.__dict__)
    save_books(books)
    print("Book added!")

def list_books():
    books = load_books()
    for b in books:
        print(f"{b['title']} by {b['author']} - ${b['price']} - Stock: {b['stock']}")
