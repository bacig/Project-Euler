from decimal import *
import time

# defines the precision to 105 decimal places
getcontext().prec = 105

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# newton-raphson's method for aproximate sqrt(n)
def my_sqrt(x: int) -> float:
        if x == 0:
              return 0
        epsilon = 1e-50
        diff = (2)
        x_1 = (x)
        x_2 = (x)//(2)
        while Decimal(diff) > Decimal(epsilon):
            x_1 = Decimal(x_2)
            x_2 = Decimal(0.5)*(Decimal(x_2) + Decimal(x) / Decimal(x_2))
            diff = abs(Decimal(x_2) - Decimal(x_1))
        return x_2

sum = 0

start = time.perf_counter()

# sum of the 100 decimal digits (includes the integer part) of the 100 irrational sqrt
for natural in range(1, 101):
      if natural not in squares:
            irrational_sqrt = str(10**(100)*my_sqrt(natural))
            for digit in range(100):
                  sum += int(irrational_sqrt[digit])

end = time.perf_counter()

print(sum, end - start)
