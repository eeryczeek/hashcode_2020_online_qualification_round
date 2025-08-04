import time
from parser import Parser
from problem import get_greedy_solution

inputs = [
    "a_example",
    "b_read_on",
    "c_incunabula",
    "d_tough_choices",
    "e_so_many_books",
    "f_libraries_of_the_world",
]
evaluation = 0
start_time = time.time()
for name in inputs:
    hashcode_problem = Parser.readHashcodeProblem(f"data/{name}.txt")
    best_solution = get_greedy_solution(hashcode_problem)
    evaluation += hashcode_problem.evaluate(best_solution)

print(f"time: {time.time() - start_time}")
print(evaluation)
