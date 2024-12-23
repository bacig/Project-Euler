import time


def fibonacci_n(n):

    fn_2 = 1
    fn_1 = 1
    fn = 0

    assert n > 0, f'A sequência de fibonacci é composta por termos positivos, o valor {n} não é positivo'

    if n == 1 or n == 2:

        return 1

    else:

        i = 1

        while i <= n-2:

            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn
            i += 1

    return fn
 

def main():

    digits = 1
    n = 1

    while digits < 1000:

        digits = len(str(fibonacci_n(n)))

        n += 1

    return n-1, fibonacci_n(n)


start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)