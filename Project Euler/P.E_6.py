def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

def square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

def main(n):
    _sum_squares = sum_squares(n)
    _square_sum  = square_sum(n)

    return _square_sum - _sum_squares

if __name__ == '__main__':
    print(main(100))