import time


def main(n):
    longest_chain = 0
    longest_chain_number = 1
    i = 1

    while i < n:
        if longest_chain < collatz_sequence(i):
            longest_chain = collatz_sequence(i)
            longest_chain_number = i

        i += 1

    return longest_chain, longest_chain_number


def collatz_sequence(n):
    chain_size = 1
    
    while n > 1: 
        if n % 2 == 0:
            n = n // 2
            chain_size += 1

        elif n % 2 != 0:
            if n == 1:
                break
            else:
                n = 3*n + 1
                chain_size += 1

    return chain_size


start = time.perf_counter()

print(main(1e6))

end = time.perf_counter()

print(end - start)
