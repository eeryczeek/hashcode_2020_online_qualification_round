from dtos import LibraryWithSelectedBooks, Solution
import time

from problem import HashcodeProblem


class SolutionEvolutionary:
    def __init__(self, problem: HashcodeProblem):
        self.problem = problem

    def initialize_greedy_solution(self, start_time: float):
        ordered_libraries = sorted(
            self.problem.libraries,
            key=lambda x: (sum([book.score for book in x.books]) / x.signup_time),
            reverse=True,
        )
        solution = Solution(libraries=[])
        days_left = self.problem.days_number
        for library in ordered_libraries:
            days_left = max(days_left - library.signup_time, 0)
            new_library = LibraryWithSelectedBooks(
                id=library.id,
                number_of_books=library.number_of_books,
                books=library.books,
                signup_time=library.signup_time,
                books_per_day=library.books_per_day,
                days_left=days_left,
                selected_books=sorted(
                    library.books, key=lambda x: x.score, reverse=True
                ),
            )
            solution.libraries.append((new_library))
        return solution, self.problem.evaluate2(solution), time.time() - start_time
