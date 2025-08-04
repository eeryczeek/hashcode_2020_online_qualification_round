import time
from parser import Parser
from solution import SolutionEvolutionary

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
    solution = SolutionEvolutionary(hashcode_problem)

    best_solution, eval, execution_time = solution.initialize_greedy_solution(
        start_time
    )
    print(f"{name}: {eval}")
    evaluation += eval

print(f"time: {time.time() - start_time}")
print(evaluation)
