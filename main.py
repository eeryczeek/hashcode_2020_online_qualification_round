import time
from book import Book
from library import Library
from problem import HashcodeProblem
from solution import SolutionEvolutionary

names = ['a_example', 'b_read_on', 'c_incunabula',
         'd_tough_choices', 'e_so_many_books', 'f_libraries_of_the_world']
evaluation = 0
start_time = time.time()

for name in names:
    with open(f"data/{name}.txt", "r") as f_in:
        lines = f_in.read().splitlines()

    _, number_of_libraries, number_of_days = map(int, lines.pop(0).split())
    books = tuple(Book(int(id), int(score))
                  for id, score in enumerate(lines.pop(0).split()))

    libraries = [
        Library(
            library_id,
            num_books,
            {books[int(book_id)] for book_id in lines.pop(0).split()},
            signup_time,
            books_per_day
        )
        for library_id in range(number_of_libraries)
        for num_books, signup_time, books_per_day in [map(int, lines.pop(0).split())]
    ]

    hashcode_problem = HashcodeProblem(
        number_of_days, number_of_libraries, libraries, books)
    solution = SolutionEvolutionary(hashcode_problem, 10, 0.6, 0.2, 0.25)
    eval, best_solution, execution_time = solution.evolution(0, start_time)
    print(f'{name}: {eval}')
    evaluation += eval

print(f'time: {time.time() - start_time}')
print(evaluation)
