from timeit import timeit


def insertion_sort(L):
    '''插入排序，升序
    相当于将L[i]与 "已排序序列" 中的元素(从后向前)依次比较，如果L[i]比较小，则交换位置
    '''
    n = len(L)
    if n == 1:
        return

    # 首先，假设第1个元素L[0]是 "已排序序列"，第2个元素L[1]至最后一个元素L[n-1]是 "未排序序列"
    for i in range(1, n):  # 共需要 n-1 次插入操作。 i 表示 "未排序序列" 的第1个元素的下标，所以 i 从下标 1 开始

        # j 的范围是 [i, i-1，... 2, 1]，即包含下标 i 和 "已排序序列" 的所有下标
        for j in range(i, 0, -1):  # 将 "未排序序列" 的第1个元素L[i]，依次与 "已排序序列" 中的所有元素比较
            if L[j] < L[j-1]:  # 如果小于前一个元素，则交换位置
                L[j], L[j-1] = L[j-1], L[j]
            else:  # 如果不小于前一个元素，则肯定不小于这个元素之前的所有元素（因为前面已排好序了），所以可以退出比较的循环
                break


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    print('Insertion sort function run 1,000,000 times, cost: ', timeit('insertion_sort(L2)', 'from __main__ import insertion_sort, L2'), 'seconds.')


# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Insertion sort function run 1,000,000 times, cost:  7.045618813 seconds.
