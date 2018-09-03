from timeit import timeit


def bubbLe_sort(L):
    '''冒泡排序，升序'''
    n = len(L)
    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作，只遍历并比较 "未排序的序列" 中的元素（会依次变少）
        # 注意 j 表示序列的下标，所以 j 的取值范围为 0, 1, 2 ... n-i-2， 不能取n-i-1，否则后续L[j+1]会下标越界
        for j in range(n-i-1):  # 助记：每次冒泡操作需要 n-i-1 次比较
            if L[j] > L[j+1]:  # 如果L[j]比L[j+1]大，则交换它们的位置
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
# Bubble sort function run 1,000,000 times, cost:  12.419256763 seconds.
