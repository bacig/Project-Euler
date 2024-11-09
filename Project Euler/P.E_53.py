import math as m
import time
import num2words


factorials = [m.factorial(i) for i in range(101)]

def combinatorics(n,r): 
    return factorials[n]//(factorials[r]*factorials[n-r])

def main():
    greater_than_1million = 0
    larger, i, j = 0, 0, 0

    for n in range(0,101):
        for r in range(0,n+1):
            if combinatorics(n,r) > int(1e6):
                greater_than_1million += 1
                if combinatorics(n,r) > larger:
                    larger, i, j = combinatorics(n,r), n, r
                
    return greater_than_1million, larger, i, j

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(end - start)