import time


def is_palindrome(n):

    n_string = str(n)
    palindrome = True

    for chr in range(len(n_string) // 2):

        if n_string[chr] != n_string[len(n_string) - chr -1]:

            palindrome = False

    return palindrome


def main():

    sum = 0

    for num in range(1, 1000000):

        if str(num)[:] == str(num)[::-1]:

            if bin(num)[2:] == bin(num)[:1:-1]:

                sum += num 

    """sum = 0

    for num in range(1, 1000000):

        if is_palindrome(num):

            if is_palindrome(bin(num)[2:]):

                if bin(num)[2] != '0':

                    sum += num"""

    return sum
 

start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)
 