from gaps import sedgewick_gaps


def shell_sort(L):
    '''希尔排序，升序
    步长序列使用 Sedgewick 提出的[1, 5, 19, 41, 109, 209, 505, 929 ...]，此时时间复杂度为 O(n (logn)^2)
    '''
    n = len(L)
    if n <= 1:
        return

    gen = sedgewick_gaps(n)  # [1, 5, 19, 41, 109, 209, 505, 929 ...]
    for gap in reversed(list(gen)):  # 将gen生成器对象转换成列表，再倒序: [41, 19, 5, 1]

        # 想像成，以步长 gap 将原始序列划分成 gap 个待排序的序列，对每个序列使用普通的插入排序进行排序
        # 序列1: [L[0], L[gap], L[2*gap]...]
        # 序列2: [L[1], L[1+gap], L[1 + 2*gap]...]
        # 序列3: [L[2], L[2+gap], L[2 + 2*gap]...]
        # 请查看插入排序算法 https://github.com/wangy8961/python3-algorithms/blob/master/4.%20%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%20-%20Insertion%20Sort/3_best_insertion_sort_asc.py
        # 助记：普通的插入排序算法中步长是 1 ，把插入排序中的步长 1 替换为 gap
        for i in range(gap, n):  # "未排序序列" 的第1个元素分别是L[gap], L[1+gap], L[2+gap] ... ，所以变量 i 表示的下标是 gap, 1+gap, 2+gap ...
            temp = L[i]
            j = i
            # j >= gap是因为后续j[j-gap]，否则下标越界
            while j >= gap and temp < L[j-gap]:
                L[j] = L[j-gap]
                j -= gap
            L[j] = temp


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    shell_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from timeit import timeit

    def shell_sort():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]

        n = len(L)
        gen = sedgewick_gaps(n)  # [1, 5, 19, 41]
        for gap in reversed(list(gen)):  # 将gen生成器对象转换成列表，再倒序: [41, 19, 5, 1]
            for i in range(gap, n):
                temp = L[i]
                j = i
                while j >= gap and temp < L[j-gap]:
                    L[j] = L[j-gap]
                    j -= gap
                L[j] = temp

        return L


    print('Shell sort function run 1000 times, cost: ', timeit('shell_sort()', 'from __main__ import shell_sort', number=1000), 'seconds.')


    # Output:
    # Shell sort function run 1000 times, cost:  0.354474 seconds.
    '''
