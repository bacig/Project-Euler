n = 2**1000
n = str(n)
digit_list = []

for i in range(len(n)):
    digit_list.append(int(n[i]))

j = 0
sum = 0

'''while j <= len(digit_list):
    sum += digit_list[j]
    j += 1'''

for j in range(len(digit_list)):
    sum += digit_list[j]

print(sum)