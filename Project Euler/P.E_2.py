def EvenFibonacciSum(n):
    
    _fib_i1 = 1
    _fib_i2 = 2
    sum = _fib_i2

    while _fib_i2 < n:
        _fib_i1 = _fib_i1 + _fib_i2
        if (_fib_i1 % 2 == 0):
            sum += _fib_i1
        _fib_i2 = _fib_i1 + _fib_i2
        if (_fib_i2 % 2 == 0 and _fib_i2 < n):
            sum += _fib_i2
    
    return sum

if __name__ == "__main__":
    print(EvenFibonacciSum(3999999))