def sedgewick_gaps(n):
    '''从小到大生成 [1, 5, 19, 41, 109, 209, 505, 929 ...]'''
    i = 0
    while True:
        gap1 = 9 * (4 ** i - 2 ** i) + 1              # 1, 19, 109, 505, 2161 ...
        gap2 = 2 ** (i + 2) * (2 ** (i + 2) - 3) + 1  # 5, 41, 209, 929, 3905 ...

        # gap1 貌似永远会比 gap2 小
        if n > gap2:  # 输出 gap1 和 gap2
            yield gap1
            yield gap2
            i += 1
        elif gap2 > n > gap1:  # 只输出 gap1
            yield gap1
            i += 1
        else:
            break
