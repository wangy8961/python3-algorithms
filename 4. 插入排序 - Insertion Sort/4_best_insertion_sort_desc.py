from timeit import timeit


def insertion_sort(L):
    '''插入排序，降序'''
    n = len(L)
    if n == 1:
        return

    for i in range(1, n):
        j = i
        while j >= 1 and L[j] > L[j-1]:  # 第1次是比较 "未排序序列" 的第1个元素和 "已排序序列" 的最后1个元素
            L[j], L[j-1] = L[j-1], L[j]
            j -= 1


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    print('Insertion sort function run 1,000,000 times, cost: ', timeit('insertion_sort(L2)', 'from __main__ import insertion_sort, L2'), 'seconds.')


# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
# Insertion sort function run 1,000,000 times, cost:  3.727573309 seconds.
