import math as m
import time

 
start = time.perf_counter()


sum_total = 0

for i in range(145,1000001):

    i_str = str(i)

    sum = 0

    for digit in i_str:

        sum += m.factorial(int(digit))

    if sum == i:

        sum_total += sum

 
end = time.perf_counter()

print(sum_total)

print(end - start)
