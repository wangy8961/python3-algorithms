from timeit import timeit


def insertion_sort(L):
    '''插入排序，升序
    相当于将L[i]与 "已排序序列" 中的元素(从后向前)依次比较，如果L[i]比较小，则交换位置
    '''
    n = len(L)
    if n == 1:
        return

    # 首先，假设第1个元素L[0]是 "已排序序列"，第2个元素L[1]至最后一个元素L[n-1]是 "未排序序列"
    for i in range(1, n):  # 未排序的元素有 n-1 个，所以共需要 n-1 次插入操作。 i 表示 "未排序序列" 的第1个元素的下标，所以 i 从下标 1 开始

        # 将 "未排序序列" 的第1个元素和 "已排序序列" 从后向前，每两个元素之间比较，如果顺序不对就交换它俩的位置
        # 使用while循环
        j = i
        # j >= 1是因为后续j[j-1]，否则下标越界
        while j >= 1 and L[j] < L[j-1]:  # 第1次是比较 "未排序序列" 的第1个元素和 "已排序序列" 的最后1个元素
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
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Insertion sort function run 1,000,000 times, cost:  3.729491712 seconds.
