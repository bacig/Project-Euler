import math as m
import time


def sum_divisors_of(n):

    divisors_sum = 0

    for num in range(1, n//2 + 1):

        if n % num == 0:

            divisors_sum += num

    return divisors_sum


def main():

    amicable_sum = 0

    for a in range(1,10000):

        if sum_divisors_of(a) != 0:

            b = sum_divisors_of(a)

            if a == sum_divisors_of(b) and a != b:

                amicable_sum = amicable_sum + a + b

    return amicable_sum//2


start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)
