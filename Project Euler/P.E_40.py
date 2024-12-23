import time


start = time.perf_counter()

constant = '0.'

for i in range(1,185186):

    constant += str(i)

temp = 1
product = 1

print(int(constant[2])*int(constant[11])*int(constant[101])*int(constant[1001])*int(constant[10001])*int(constant[100001])*int(constant[1000001]))


end = time.perf_counter()

print(end - start)
