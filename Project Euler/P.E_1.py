import time


def main(n):
    i = 1
    sum = 0
   
    while i < n:
        if (i%3 == 0 or i%5 == 0):
            sum += i
   
        i += 1
   
    return sum


start = time.perf_counter()

print(main(1000))
    
end = time.perf_counter()

print(end - start)