import random
import numpy as np


class Library:

    days_left = None
    unique_books = set()

    def __init__(self, id, number_of_books, books, signup_time, books_per_day):
        self.id = id
        self.number_of_books = number_of_books
        self.books = books
        self.signup_time = signup_time
        self.books_per_day = books_per_day

    def choose_random_books(self):
        if self.days_left == 0:
            return set()
        books = set(random.sample(self.books, min(
            self.number_of_books, self.books_per_day * self.days_left)))
        return books

    def choose_greedy_books(self, read):
        chosen = set()
        if self.days_left == 0:
            return set()

        books = sorted(list(self.books), key=lambda x: x.score, reverse=True)
        for book in books:
            if len(chosen) == self.days_left*self.books_per_day:
                return chosen

            if book not in read:
                chosen.add(book)
                read.add(book)
        return chosen

    def mutate_books(self, chosen_books):
        if len(chosen_books) == self.number_of_books or len(chosen_books) == 0:
            return chosen_books

        books_to_choose_from = self.books - chosen_books
        n = np.random.randint(
            1, min(len(books_to_choose_from), len(chosen_books))+1)

        books_to_remove = random.sample(chosen_books, n)
        books_to_add = random.sample(books_to_choose_from, n)

        chosen_books.difference_update(books_to_remove)
        chosen_books.update(books_to_add)
        return chosen_books

    def fix_books(self, chosen_books):
        if self.days_left == 0:
            return set()

        delta = min(self.days_left * self.books_per_day,
                    self.number_of_books) - len(chosen_books)

        if delta > 0:
            chosen_books.update(random.sample(
                self.books - chosen_books, delta))
            return chosen_books

        if delta < 0:
            chosen_books.difference_update(random.sample(chosen_books, -delta))
            return chosen_books

        return chosen_books
