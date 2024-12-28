import time
 

def permutation_checker(x):
    x_digits = list(str(x))
 
    for digit in list(str(2*x)):
        if digit not in x_digits:

            return False
       
    for digit in list(str(3*x)):
        if digit not in x_digits:

            return False
 
    for digit in list(str(4*x)):
        if digit not in x_digits:

            return False

    for digit in list(str(5*x)):
        if digit not in x_digits:

            return False

    for digit in list(str(6*x)):
        if digit not in x_digits:

            return False

    return True


permuted_multiple = False
n = 1

start = time.perf_counter()

while not permuted_multiple:
    if permutation_checker(n) is True:
        print(n)

        end = time.perf_counter()
        
        break

    n += 1

print(end - start)
