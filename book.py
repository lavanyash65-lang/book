def book_details(title, author, isbn, price):
    result = (
        f"Book Title: {title}\n"
        f"Author: {author}\n"
        f"ISBN: {isbn}\n"
        f"Price: {price}"
    )
    return result

if __name__ == "__main__":
    title = "Python Basics"
    author = "John Doe"
    isbn = "978-1234567890"
    price = 499
    print(book_details(title, author, isbn, price))
