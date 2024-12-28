import time
# sympy's isprime is about 20 times faster here
from sympy import isprime


def is_prime(n):
    i = 2
    prime = True

    if n == 0 or n == 1:
        prime = False

        return prime
  
    while i <= n**(1/2):
        if n % i == 0:
            prime = False
            break

        i += 1

    return prime


def main(n):
    i = 0  
    sum = 0

    while i < n:
        if isprime(i):
            sum += i
        i += 1

    return sum


start = time.perf_counter()

print(main(2*10**6))

end = time.perf_counter()

print(end - start)
