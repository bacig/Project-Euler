import time
from itertools import permutations

start = time.perf_counter()

permutation = list(permutations('0123456789', 10))

permutation = permutation[362880:]

target = []

for number in permutation:
    if int(number[3]) % 2 == 0:
        if int(number[2] + number[3] + number[4]) % 3 == 0:
            if int(number[5]) % 5 == 0:
                if int(number[4] + number[5] + number[6]) % 7 == 0:
                    if int(number[5] + number[6] + number[7]) % 11 == 0:
                        if int(number[6] + number[7] + number[8]) % 13 == 0:
                            if int(number[7] + number[8] + number[9]) % 17 == 0:
                                target.append(number)

sum = 0

for number in target:
    temp = ''
    for digit in number:
        temp += digit
    sum += int(temp)

end = time.perf_counter()

print(target)
print(sum)
print(end - start) 