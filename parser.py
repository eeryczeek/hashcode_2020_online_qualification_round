from dtos import Book, Library
from problem import HashcodeProblem


class Parser:

    @staticmethod
    def readHashcodeProblem(path: str) -> HashcodeProblem:
        with open(path, "r") as f_in:
            lines = f_in.read().splitlines()

        books_number, libraries_number, days_number = map(int, lines.pop(0).split())
        books = tuple(
            Book(id, int(score)) for id, score in enumerate(lines.pop(0).split())
        )

        libraries = [
            Library(
                id=library_id,
                signup_time=signup_time,
                books_per_day=books_per_day,
                number_of_books=num_books,
                books={books[int(book_id)] for book_id in lines.pop(0).split()},
            )
            for library_id in range(libraries_number)
            for num_books, signup_time, books_per_day in [
                map(int, lines.pop(0).split())
            ]
        ]

        return HashcodeProblem(
            books_number=books_number,
            libraries_number=libraries_number,
            days_number=days_number,
            libraries=libraries,
            books=books,
        )
