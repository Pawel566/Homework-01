class Book:
    def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        #nie dodałem obsługi wyjątków, po próbie program nie działa

    @staticmethod
    def check_isbn(isbn):
        if len(isbn) not in (10, 13):
            return False
        if len(isbn) == 10:
            result = 0
            for i in range(9):
                result += int(isbn[i]) * (1 if i % 2 == 0 else 3)
            return (result % 11) == int(isbn[9])

        if len(isbn) == 13:
            result = 0
            for i in range(12):
                result += int(isbn[i]) * (1 if i % 2 == 0 else 3)
            return (result % 10) == int(isbn[12])

        return False

    def __str__(self):
        return f"Książka: {self.title}, Autor: {self.author}, ISBN: {self.isbn}"


book_1 = Book("Ojciec chrzestny", "Mario Puzo", "9781785151781")
print(book_1)
book_2 = Book("Moje próby programowania", "Ja", "1234567891")
print(book_2)
