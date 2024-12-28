import time


def main():
    max_sum = 0

    for i in range(1, 101):
        for j in range(1, 101):
            if digit_sum(i**j) > max_sum:
                max_sum = digit_sum(i**j)

    return max_sum


def digit_sum(n):
    n_str = str(n)
    sum = 0 

    for i in range(0,len(n_str)):
        sum += int(n_str[i])

    return sum

start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)
