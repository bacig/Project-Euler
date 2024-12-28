import time


start = time.perf_counter()

sum = 0

for i in range(1,1001):
    sum = sum + i**i

sum_str = str(sum)

end = time.perf_counter()

print(sum_str)

print(end - start)
