def quick_sort(L):
    '''使用 '列表生成式(List Comprehensions)' 查找比 '基准(pivot)' 小或大的元素序列'''
    n = len(L)
    if n <= 1:
        return L

    pivot_value = L[0]
    lesser = [item for item in L[1:] if item <= pivot_value]
    greater = [item for item in L[1:] if item > pivot_value]

    return quick_sort(lesser) + [pivot_value] + quick_sort(greater)


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    # 也可以将 quick_sort(L) 改写成一行：
    # quick_sort = lambda L: L if len(L) <= 1 else quick_sort([i for i in L[1:] if i <= L[0]]) + [L[0]] + quick_sort([j for j in L[1:] if j > L[0]])
    sorted = quick_sort(L1)
    print('After: ', sorted)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from timeit import timeit

    def test():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
        quick_sort(L)

    def quick_sort(L):
        n = len(L)
        if n <= 1:
            return L

        pivot_value = L[0]
        lesser = [item for item in L[1:] if item <= pivot_value]
        greater = [item for item in L[1:] if item > pivot_value]

        return quick_sort(lesser) + [pivot_value] + quick_sort(greater)


    print('Quick sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')


    # Output:
    # Quick sort function run 1000 times, cost:  0.2375717348850251 seconds.
    '''
