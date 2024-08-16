class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class BookStorage:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        book = Book(title, author, price)
        self.books.append(book)
        print(f"Added '{title}' by {author} to the book storage.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def update_book(self, title, new_price):
        book = self.find_book(title)
        if book:
            book.price = new_price
            print(f"Updated price of '{title}' to ${new_price}.")
        else:
            print(f"'{title}' not found in the book storage.")

    def remove_book(self, title):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Removed '{title}' from the book storage.")
        else:
            print(f"'{title}' not found in the book storage.")

    def display_books(self):
        print("Books in the storage:")
        for book in self.books:
            print(f"'{book.title}' by {book.author} (${book.price})")

# Example usage
if __name__ == "__main__":
    book_storage = BookStorage()

    book_storage.add_book("The Great Gatsby", "F. Scott Fitzgerald", 12.99)
    book_storage.add_book("To Kill a Mockingbird", "Harper Lee", 10.49)

    book_storage.update_book("The Great Gatsby", 14.99)

    book_storage.display_books()

    book_storage.remove_book("To Kill a Mockingbird")

    book_storage.display_books()
