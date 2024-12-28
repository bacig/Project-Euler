import time


start = time.perf_counter()

num_list = [num for num in range(1, 1001**2)]
leap_distance = 2
leap_count = 0
num = 1
sum = 1

while num <= len(num_list):
    if leap_count == 4:
        leap_distance += 2
        leap_count = 0
    leap_count += 1
    num += leap_distance
    sum += num

print(sum)

end = time.perf_counter()

print(end - start)
