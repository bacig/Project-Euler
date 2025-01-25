import time

start = time.perf_counter()

sieve_num = [0, 1, 2, 5, 12, 29]

for i in range(5, 1002):
    former = sieve_num[i-1]
    current = sieve_num[i]
    coming = 2*current + former
    sieve_num.append(coming)

numerators = sieve_num[1:1001]

denominators = sieve_num[2:1002]

expansions = []

for i in range(1000):
    expansions.append((numerators[i] + denominators[i], denominators[i]))

count = 0

for expansion in expansions:
    if len(str(expansion[0])) > len(str(expansion[1])):
        count += 1

end = time.perf_counter()

print(count)
print(end - start)