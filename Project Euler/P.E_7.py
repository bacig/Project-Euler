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
    j = 1
    while i < n:
        if is_prime(j):
            i += 1
        j += 1
    return j-1


print(main(10001))