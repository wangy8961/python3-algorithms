def bubbLe_sort(L):
    '''优化后的冒泡排序，升序
    最优时间复杂度为O(n)，比如L本身就是排好序的：[17, 20, 26, 31, 44, 54, 55, 77, 93]
    最坏时间复杂度还是O(n^2)
    '''
    n = len(L)
    if n <= 1:
        return

    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                flag = True
        if not flag:  # 如果我们在某一次冒泡操作中，内层遍历后发现没有交换任何元素位置，则说明此时列表已经是排序好了
            return


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from timeit import timeit

    def bubbLe_sort():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
        # L = list(range(1, 101))  # 1...100的顺序整数列表，此时是最优时间复杂度O(n)

        n = len(L)
        for i in range(n-1):
            flag = False
            for j in range(n-i-1):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    flag = True
            if not flag:
                break

        return L


    print('Bubble sort function run 1000 times, cost: ', timeit('bubbLe_sort()', 'from __main__ import bubbLe_sort', number=1000), 'seconds.')


    # Output:
    # Bubble sort function run 1000 times, cost:  1.857605113 seconds.
    # 上面的结果好像跟优化前的冒泡算法性能差不多，但是假如传入已经按 "升序" 排列好的列表，此时优化后的算法是最优时间复杂度O(n)
    # L = list(range(1, 101))，结果为：
    # Bubble sort function 03 run 1000 times, cost:  0.02233853000000008 seconds.
    '''
