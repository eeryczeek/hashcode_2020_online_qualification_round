import numpy as np
from library import Library


class HashcodeProblem():
    def __init__(self, days, number_of_libraries, libraries, books):
        self.days = days
        self.number_of_libraries = number_of_libraries
        self.libraries = libraries
        self.books = books

    def random_solution(self):
        solution = []
        days_left = self.days
        for library in np.random.permutation(self.libraries):
            new_library = Library(library.id, library.number_of_books,
                                  library.books, library.signup_time, library.books_per_day)
            days_left = max(days_left - library.signup_time, 0)
            new_library.days_left = days_left
            new_books = new_library.choose_random_books()
            solution.append((new_library, new_books))
        return solution

    def evaluate(self, solution) -> int:
        set_of_books = set()
        for library, books in solution:
            set_of_books.update(books)
        return sum(book.score for book in set_of_books)
