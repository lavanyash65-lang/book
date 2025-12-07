from book import book_details

def test_book_details():
    expected_output = (
        "Book Title: Python Basics\n"
        "Author: John Doe\n"
        "ISBN: 978-1234567890\n"
        "Price: 499"
    )
    assert book_details("Python Basics", "John Doe", "978-1234567890", 499) == expected_output
