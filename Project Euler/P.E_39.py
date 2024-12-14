import math
import numpy as np

solutions = [[perimeter, 0] for perimeter in range(1,1001)]

def valid_solution(a : int, b : int) -> list[bool, int] | bool:
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    if c % 1 == 0:
        p = a + b + int(c)
        if p <= 1000:
            return [True, p]
    return [False, 0]
            
for a in range(1,500):
    for b in range(1, 500):
        solution = valid_solution(a,b)
        if solution[0]:
            solutions[solution[1] - 1][1] += 1 

perimeter, largest = 0, 0

for solution in solutions:
    if solution[1] > largest:
        perimeter, largest = solution[0], solution[1]

print(perimeter, largest)
