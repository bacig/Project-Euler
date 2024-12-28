import time


start = time.perf_counter()

sum_total = 0

for i in range(10,999999):
    i_str = str(i)
    sum = 0

    for digit in i_str:
        sum += int(digit)**5

    if sum == i:
        sum_total += sum


end = time.perf_counter()

print(int(sum_total))

print(end - start)
