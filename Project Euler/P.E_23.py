import time
from sympy import divisors


abundant_nums = []

start = time.perf_counter()

for num in range(1, 28124):
    num_divs = divisors(num)[:-1]
    if sum(num_divs) > num:
        abundant_nums.append(num)

end = time.perf_counter()


print(abundant_nums)


print(end - start)
