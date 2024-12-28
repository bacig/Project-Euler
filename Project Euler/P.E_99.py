import time
import math as m

with open(r"C:\Users\bacig\OneDrive\Documentos\Python Scripts\P.E_99_base_exp.txt", "r") as f:
        data_read = f.read()

def main():
    file = []
    pair = []
    number = ''
    i = 0

    while i <= len(data_read):
        try:
            if data_read[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                number += data_read[i]
                i += 1
            elif data_read[i] == ',':
                pair.append(int(number))
                number = ''
                i += 1
            else:
                pair.append(int(number))
                number = ''
                file.append(pair)
                pair = []
                i += 1
        except IndexError:
            file.append([13846,725685])
            break

    largest_pair, base, expoent, line = 0, 0, 0, 0
    line_count = 1
    
    for row in file:
        if row[1]*m.log(row[0]) > largest_pair:
            largest_pair, base, expoent, line = row[1]*m.log(row[0]), row[0], row[1], line_count
        line_count += 1

    return largest_pair, base, expoent, line

start = time.perf_counter()

print(main())

end = time.perf_counter()

print(end - start)
