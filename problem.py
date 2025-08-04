from dataclasses import dataclass
from typing import List, Set
from dtos import Book, Library, LibraryWithSelectedBooks, Solution


@dataclass
class HashcodeProblem:
    books_number: int
    libraries_number: int
    days_number: int
    libraries: List[Library]
    books: tuple[Book, ...]

    def evaluate(self, solution: Solution) -> int:
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


def get_greedy_solution(problem: HashcodeProblem) -> Solution:
    ordered_libraries = sorted(
        problem.libraries,
        key=lambda x: (sum([book.score for book in x.books]) / x.signup_time),
        reverse=True,
    )
    solution = Solution(libraries=[])
    days_left = problem.days_number
    for library in ordered_libraries:
        days_left = max(days_left - library.signup_time, 0)
        new_library = LibraryWithSelectedBooks(
            id=library.id,
            number_of_books=library.number_of_books,
            books=library.books,
            signup_time=library.signup_time,
            books_per_day=library.books_per_day,
            days_left=days_left,
            selected_books=sorted(library.books, key=lambda x: x.score, reverse=True),
        )
        solution.libraries.append((new_library))
    return solution
