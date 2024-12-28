import time


def is_palindrome(n):
    n_string = str(n)
    palindrome = True

    for chr in range(len(n_string) // 2):
        if n_string[chr] != n_string[len(n_string) - chr - 1]:
            palindrome = False

    return palindrome


def reverse_number(n):
    reverse = 0

    while n != 0:
        last_digit = n % 10
        reverse = 10 * reverse + last_digit 
        n = n // 10

    return reverse


def is_lychrel(n):
    lychrel = True
    i = 0

    while i < 50 and lychrel == True:
        n = n + reverse_number(n)
        if is_palindrome(n):
            lychrel = False
        i += 1
        
    return lychrel

def main():
    count = 0

    for num in range(1,10001):
        if is_lychrel(num) == True:
            count += 1
    
    return count


start = time.perf_counter()

print(main())  

end = time.perf_counter()

print(end - start)
