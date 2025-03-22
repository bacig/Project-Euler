import time
from sympy import divisors


abundant_nums = []

start = time.perf_counter()

for num in range(1, 28124):
    num_divs = divisors(num)[:-1]
    if sum(num_divs) > num:
        abundant_nums.append(num)

sum2abundants = []

i, j = 0, 0

while i < len(abundant_nums):
    while j < len(abundant_nums):
        if abundant_nums[i] + abundant_nums[j] <= 28123:
            sum2abundants.append(abundant_nums[i] + abundant_nums[j])
        j += 1
    i += 1
    j = i

sum2abundants = list(set(sum2abundants))

print((28123 + 1)*28123//2 - sum(sum2abundants) )

end = time.perf_counter()

print(end - start)
