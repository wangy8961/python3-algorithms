def selection_sort(L):
    '''选择排序，升序'''
    n = len(L)
    if n <= 1:
        return

    for i in range(n-1):  # 共需要n-1次选择操作
        min_index = i  # 首先假设 "未排序列表"(上图中非绿色框) 的最小元素是它的第1个元素，第1次选择操作则假设L[0]是最小的，第2次操作则假设L[1]是最小的

        for j in range(i+1, n):  # 找出 "未排序列表" 中真正的最小元素的下标
            if L[j] < L[min_index]:
                min_index = j

        if min_index != i:  # 如果 "未排序列表" 中真正的最小元素，不是之前假设的元素，则进行交换
            L[i], L[min_index] = L[min_index], L[i]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    selection_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from timeit import timeit

    def selection_sort():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]

        n = len(L)
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if L[j] < L[min_index]:
                    min_index = j

            if min_index != i:
                L[i], L[min_index] = L[min_index], L[i]

        return L


    print('Selection sort function run 1000 times, cost: ', timeit('selection_sort()', 'from __main__ import selection_sort', number=1000), 'seconds.')


    # Output:
    # Selection sort function run 1000 times, cost:  0.824085003 seconds.
    '''
