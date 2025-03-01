import time

start = time.perf_counter()

def is_prime(n):
    prime = True

    if n >= 2:
        for i in range(2, int(n**(1/2)) + 1):
            if n % i == 0:

                return False
    else:
        return False

    return prime


def prime_sequence(a,b):
    
    x = 0
    count = 0
    sequence = True
    while sequence:
        y = x**2 + a*x + b
        y = round(y)
        if is_prime(y):
            count += 1
        else:
            sequence = False
            break
        x += 1

    return count


b = [i for i in range(2, 1001) if is_prime(i)]
a = [i for i in range(-999, 1000, 1)]

largest_count = 0
largest_sequence = []
largest_coefficients = 0,0

for i in a:
    for j in b:
        if prime_sequence(i, j) > largest_count:
            largest_count = prime_sequence(i, j)
            largest_coefficients = i, j

end = time.perf_counter()

print(largest_coefficients[0]*largest_coefficients[1])
print(end - start)