import math
import time
# sympy's is about 10 times faster here
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


def remove_right(n):
    temp = n

    while len(str(temp)) > 1:
        if not isprime(temp): return 0

        temp = temp // 10

    if isprime(temp): return 1 
    
    else: return 0


def remove_left(n):
    temp = n

    while len(str(temp)) > 1:
        if not isprime(temp): return 0

        temp = temp % 10 ** (len(str(temp)) - 1)

    if isprime(temp): return 1
        
    else: return 0
        

i = 23
sum = 0
truncable_primes = 0
truncable_primes_list = []

start = time.perf_counter()

while truncable_primes < 11:
    if remove_right(i) != 0:
        if remove_left(i) != 0:
            sum += i    
            truncable_primes += 1
            truncable_primes_list.append(i)
    i += 1

end = time.perf_counter()

print(sum, truncable_primes_list)

print(end - start)
