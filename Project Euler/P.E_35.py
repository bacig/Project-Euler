import math
import time
# sympy's isprime is about 15 times faster here
from sympy import isprime


def is_prime(n):
    i = 2
    prime = True

    if n == 0 or n == 1:
        prime = False

        return prime
  
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            prime = False
            break
 
        i += 1

    return prime

def rotate(n):
    rotation = 0
    temp = n

    while rotation < len(str(n)):
        if not isprime(temp):

            return 0

        temp = (temp % 10) * 10 **(len(str(temp)) - 1) + temp // 10
        rotation += 1

    return 1

circular_primes = 4

start = time.perf_counter()

for i in range(11, int(1e6), 2):
    if rotate(i) == 1:
        circular_primes += 1

end = time.perf_counter()

print(circular_primes)

print(end - start)
