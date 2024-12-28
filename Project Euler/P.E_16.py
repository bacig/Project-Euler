import time


start = time.perf_counter()

n = 2**1000
n = str(n)
digit_list = []

for i in range(len(n)):
    digit_list.append(int(n[i]))

j = 0
sum = 0

for j in range(len(digit_list)):
    sum += digit_list[j]

end = time.perf_counter()

print(sum)

print(end - start)
