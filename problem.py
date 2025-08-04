from dataclasses import dataclass
from typing import List, Set
from dtos import Book, Library, Solution


@dataclass
class HashcodeProblem:
    books_number: int
    libraries_number: int
    days_number: int
    libraries: List[Library]
    books: tuple[Book, ...]

    def evaluate2(self, solution: Solution) -> int:
        shared_set_of_books: Set[Book] = set()
        for library in solution.libraries:
            selected_books = [
                book
                for book in library.selected_books
                if book not in shared_set_of_books
            ]
            shared_set_of_books.update(
                selected_books[: library.days_left * library.books_per_day]
            )

        return sum(book.score for book in shared_set_of_books)
