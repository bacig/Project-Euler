import time

def main():
    largest_palindrome = 0,0,0
    
    for i in range(100,999):
        for j in range(100,999):
            if is_palindrome(i*j):
                if largest_palindrome[0] < i*j:
                    largest_palindrome = i*j,i,j

    return largest_palindrome

def is_palindrome(n):
    palindrome = False
    n = str(n)

    if len(n) == 6:
        if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
            palindrome = True
    
    return palindrome

start = time.perf_counter()
print(main())
end = time.perf_counter()
print(end - start)
