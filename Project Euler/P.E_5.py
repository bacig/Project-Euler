def main():
    i = 2520

    while is_divisible(i) == False:
        i += 1

    return i

def is_divisible(n):
    multiple = True

    for i in range(2,20):
        if n % i != 0:
            multiple = False
            break

    return multiple


print(main())
