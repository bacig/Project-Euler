import time


start = time.perf_counter()

power_array = [[pow(i,j) for j in range(2,101)] for i in range(2,101)]
power_list = []


for i in range(99):

    for j in range(99):

        power_list.append(power_array[i][j])


print(len(list(set(sorted(power_list)))))

end = time.perf_counter()

print(end - start)
