class Book:
    total_books = 0

    def __init__(self,title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


Book1 = Book("Web Programming")
Book2 = Book("Web Development")
print(f'Total books created: {Book.total_books}')