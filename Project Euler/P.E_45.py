import time


def tph():
    tph = False
    n = 143
    t_list = [1]
    p_list = [1]
    h_list = [1]
 
    while tph is False:
        n += 1
        t = n * (n + 1) // 2
        t_list.append(t)
        p = n * (3 * n - 1) // 2
        p_list.append(p)
        h = n * (2 * n - 1)
        h_list.append(h)

        if t in p_list:
            if t in h_list:
                if t != 40755:
                    tph = True

    return t, n


start = time.perf_counter()

print(tph())

end = time.perf_counter()

print(end - start)
