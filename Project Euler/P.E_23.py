import time


def divisibles(n):
    divs =  []
    i = 1

    while i <= n//2:
        if n % i == 0:
            divs.append(i)
        i += 1

    return divs

def sum_list(n):
    sum = 0

    for i in n:
        sum += i

    return sum


def main(n):
    sum = 0
    i = 1

    while i <= n:
        if sum_list(divisibles(i)) <= i:
            sum += i
        i += 1
    
    return sum


start = time.perf_counter()

print(main(28123))

end = time.perf_counter()

print(end - start)
