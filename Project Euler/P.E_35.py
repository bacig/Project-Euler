import math as m

def is_prime(n: int) -> bool:
    prime = True

    for i in range(2,int(m.sqrt(n)) + 1):
        if n % i == 0:
            prime = False
    
    return prime

memo: list = []

for i in range(2, 1000001):
    if is_prime(i) == True:
        memo.append(i)

memo2 = [num for num in memo if all(int(digit) % 2 != 0 for digit in str(num))]

counts = 0
for prime in memo2:
    temp = ''
    circular = True
    rotations = 0
    while circular == True and rotations < len(str(prime)):
        temp = ''
        temp = str(prime)[-1] + str(prime)[0:len(str(prime)) - 2]

print(memo2)