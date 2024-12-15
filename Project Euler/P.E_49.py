import time
import math
from itertools import permutations as perm
from itertools import combinations as comb

def is_prime(n):
    i = 2
    prime = True
    if n == 0 or n == 1:
        prime = False
        return prime
  
    while i <= math.sqrt(n):
        if n % i == 0:
            prime = False
            break
        i += 1
    return prime

def prime_permutation(prime):
    permutations = list(set(perm(str(prime))))
    temp = []
    for permutation in permutations:
        if permutation[0] == '0':
            continue
        temp_str = ''
        i = 0
        while i < 4:
            temp_str += permutation[i]
            i += 1
        temp.append(int(temp_str))
    return temp

start = time.perf_counter()

primes = [prime for prime in range(1000,9999) if is_prime(prime)]
sequence = []
for prime in primes:
    permutation = prime_permutation(prime)
    primes_in_permutation = [number for number in permutation if is_prime(number)]    
    if len(primes_in_permutation) >= 3:
        combinations_by_three = list(comb(primes_in_permutation, 3))
        for combination in combinations_by_three:
            triple = sorted(combination)
            if triple[2] - triple[1] == triple[1] - triple[0]:
                sequence.append(triple)
                break
        

print(sequence)

end = time.perf_counter()
print(end - start)