def bubbLe_sort(L):
    '''冒泡排序，升序'''
    n = len(L)
    if n <= 1:
        return

    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作，只遍历并比较 "未排序的序列" 中的元素（会依次变少）
        # 注意 j 表示序列的下标，所以 j 的取值范围为 0, 1, 2 ... n-i-2， 不能取n-i-1，否则后续L[j+1]会下标越界
        for j in range(n-i-1):  # 助记：每次冒泡操作需要 n-i-1 次比较
            if L[j] > L[j+1]:  # 如果L[j]比L[j+1]大，则交换它们的位置
                L[j], L[j+1] = L[j+1], L[j]


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

        n = len(L)
        for i in range(n-1):
           for j in range(n-i-1):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]

        return L


    print('Bubble sort function run 1000 times, cost: ', timeit('bubbLe_sort()', 'from __main__ import bubbLe_sort', number=1000), 'seconds.')


    # Output:
    # Bubble sort function run 1000 times, cost:  1.853806487 seconds.
    '''
