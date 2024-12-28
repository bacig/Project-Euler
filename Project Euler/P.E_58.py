import math
import time
from sympy import isprime


def is_prime(n):

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:

            return False

    return True


right_diagonal = [3,7]
right_leap = 6

left_diagonal = [5,9]
left_leap = 8

ratio = 1
square_length = 3
count = 3

start = time.perf_counter()

while ratio > 0.1:   
    #right_diagonal
    right_diagonal.append(right_diagonal[-1] + right_leap)
    right_leap += 2
    right_diagonal.append(right_diagonal[-1] + right_leap)
    right_leap += 2
 

    if isprime(right_diagonal[-2]) == True:
        count += 1

    if isprime(right_diagonal[-1]) == True:
        count += 1

    #left_diagonal
    left_diagonal.append(left_diagonal[-1] + left_leap)
    left_diagonal.append(left_diagonal[-1] + left_leap)
    left_leap += 4
 

    if isprime(left_diagonal[-2]) == True:
        count += 1

    if isprime(left_diagonal[-1]) == True:
        count += 1

    square_length += 2
    ratio = count / (2*square_length - 1)
   

end = time.perf_counter()

print(end - start)
