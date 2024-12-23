import math as m
import time

 
def is_prime(n):

    prime = True

    if n >= 2:

        for i in range(2, int(m.sqrt(n)) + 1):

            if n % i == 0:

                return False

    else:

        return False

    return prime


start = time.perf_counter()

primes_below_1million = [primes_below_1million for primes_below_1million in range(1,1_000_000) if is_prime(primes_below_1million)]

end = time.perf_counter()

print(end - start)
