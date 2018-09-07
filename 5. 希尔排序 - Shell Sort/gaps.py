def sedgewick_gaps(n):
    '''从小到大生成 [1, 5, 19, 41, 109, 209, 505, 929 ...]'''
    i = 0
    while True:
        gap1 = 9 * (4 ** i - 2 ** i) + 1
        gap2 = 2 ** (i + 2) * (2 ** (i + 2) - 3) + 1

        if n > gap1 or n > gap2:
            if gap1 < gap2:  # gap1貌似永远会比gap2大
                yield gap1
                yield gap2
            else:
                yield gap2
                yield gap1
            i += 1
        else:
            break
