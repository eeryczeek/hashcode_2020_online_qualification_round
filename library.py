import random
import numpy as np


class Library:
    def __init__(self, id, number_of_books, books, signup_time, books_per_day):
        self.id = id
        self.number_of_books = number_of_books
        self.books = books
        self.signup_time = signup_time
        self.books_per_day = books_per_day
        self.days_left = None
        self.unique_books = set()

    def choose_random_books(self):
        if self.days_left == 0:
            return set()
        books = set(random.sample(self.books, min(
            self.number_of_books, self.books_per_day * self.days_left)))
        return books

    def choose_greedy_books(self, read):
        if self.days_left == 0:
            return set(), read

        books = sorted((book for book in self.books if book not in read),
                       key=lambda x: x.score, reverse=True)
        chosen = set(books[:self.days_left*self.books_per_day])
        read.update(chosen)
        return chosen, read

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
