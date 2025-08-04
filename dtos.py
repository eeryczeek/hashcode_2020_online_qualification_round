from dataclasses import dataclass, field
from typing import List, Set


@dataclass(frozen=True)
class Book:
    """Represents a book with an ID and a score."""

    id: int
    score: int


@dataclass(frozen=True)
class Library:
    """Represents the static data for a library."""

    id: int
    signup_time: int
    books_per_day: int
    number_of_books: int
    books: Set[Book] = field(default_factory=set, compare=False, hash=False)


@dataclass(frozen=True)
class LibraryWithSelectedBooks(Library):
    """Represents a library with selected books for a solution."""

    days_left: int = 0
    selected_books: List[Book] = field(default_factory=list, compare=False, hash=False)


@dataclass
class HashcodeProblem:
    books_number: int
    libraries_number: int
    days_number: int
    number_of_libraries: int
    libraries: List[Library]
    books: tuple[Book]


@dataclass
class Solution:
    libraries: List[LibraryWithSelectedBooks]
