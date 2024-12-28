import math as m
import itertools
import time

memo: list = [2,3,5,7]

def is_prime(n):
    prime = True

    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break

    return prime

 
def main():
    seven_digit_permutations = list(itertools.permutations([i for i in range(1,8)]))

    for number in range(len(seven_digit_permutations), 1, -1):
        permutation = ''
        for digit in seven_digit_permutations[number - 1]:
            permutation += str(digit)
        if is_prime(int(permutation)) == True:

            return permutation


start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)
