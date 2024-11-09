import math as m
import time
import sys

sys.set_int_max_str_digits(0)

start = time.time()
marsenne_prime = (28433 * 2**7830457 + 1) % 10 ** 10
end = time.time()

print((marsenne_prime))

print(f"Task completed in {end - start} s")
