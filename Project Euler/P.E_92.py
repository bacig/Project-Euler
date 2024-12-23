import time


def chain(num):

    if num in [44, 32, 13, 10, 1, 7, 10, 19, 23, 28, 31, 49, 68, 70, 79, 82, 86, 91, 94, 97]:

        return 1

    elif num in [85, 89, 145, 42, 20, 4, 16, 37, 58, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18]:

        return 89

    else:

        num_str = str(num)
        temp = 0

        for digit in num_str:

            temp += int(digit)**2

        return chain(temp)
 

start = time.perf_counter()


_89_count = 0
_1_count = 0  

for number in range(2, int(1e7)):

    if chain(number) == 1:

        _1_count += 1

    else:

        _89_count += 1
        print(_89_count)

"""for number in range(2,100):

    if chain(number) == 1:

        print(f"o número {number} termina em 1")

    else:

        print(f"o número {number} termina em 89")"""


print(f"{_89_count} números acabam em 89 e {_1_count} números acabam em 1.")

end = time.perf_counter()

print(end - start)
