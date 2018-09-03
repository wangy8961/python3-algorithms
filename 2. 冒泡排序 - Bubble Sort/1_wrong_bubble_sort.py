from timeit import timeit


def bubbLe_sort(L):
    '''演示错误的冒泡算法'''
    n = len(L)
    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作都遍历整个列表的元素，即使后面已经排序好的元素也会比较，完全是在浪费时间
        for j in range(n-1):  # j 表示列表的下标，j不能取值n-1，否则L[j+1]会下标越界
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    print('Bubble sort function run 1,000,000 times, cost: ', timeit('bubbLe_sort(L2)', 'from __main__ import bubbLe_sort, L2'), 'seconds.')


# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Bubble sort function run 1,000,000 times, cost:  18.196879405 seconds.
