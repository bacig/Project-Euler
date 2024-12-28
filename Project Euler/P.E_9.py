import time


a = 499
b = 1

start = time.perf_counter()

while a > 1:
    print(f"a =  {(1000*(b - 500)/(b - 1000))}, b = {b}")
    a -= 1
    b += 1

end = time.perf_counter()

print(end - start)