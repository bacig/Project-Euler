import random as rd
import itertools
import time


start = time.perf_counter()

print(sorted(list(itertools.permutations(range(10),10)))[999999])

end = time.perf_counter()
