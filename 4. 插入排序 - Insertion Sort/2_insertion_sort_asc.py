from timeit import timeit


def insertion_sort(L):
    '''插入排序，升序
    相当于将L[i]提起来，再与 "已排序序列" 中的元素(从后向前)依次比较，
    如果L[i]比较小，则将 "已排序序列" 中的元素依次往后挪一个位置
    '''
    n = len(L)
    if n == 1:
        return

    for i in range(1, n):
        '''
        第3次插入的过程：

        i = 3，此时列表为 [26, 54, 93, 17, 77, 31, 44, 55, 20]，"已排序序列" 为[26, 54, 93]，"未排序序列" 为[17, 77, 31, 44, 55, 20]
        temp = L[3]  # 17

        j = i - 1  # 2
        此时，while条件为True，L[j+1] = L[j]，即L[3] = L[2] = 93，会覆盖之前的17，所以temp变量的作用就是先保留该值
        列表变为 [26, 54, 93, 93, 77, 31, 44, 55, 20]

        j -= 1  # 1
        此时，while条件为True，L[j+1] = L[j]，即L[2] = L[1] = 54
        列表变为 [26, 54, 54, 93, 77, 31, 44, 55, 20]

        j -= 1  # 0
        此时，while条件为True，L[j+1] = L[j]，即L[1] = L[0] = 26
        列表变为 [26, 26, 54, 93, 77, 31, 44, 55, 20]

        j -= 1  # -1
        此时，while条件为False，L[j+1] = temp，即L[0] = temp = 17
        列表变为 [17, 26, 54, 93, 77, 31, 44, 55, 20]
        至此，已将 "未排序序列" [17, 77, 31, 44, 55, 20] 的第1个元素17插入到 "已排序序列" [26, 54, 93] 的正确位置
        '''

        temp = L[i]  # "未排序序列" 的第1个元素
        j = i - 1  # "已排序序列" 的最后1个元素，因为要从后向前比较 "已排序序列"
        while j >= 0 and temp < L[j]:  # 如果 "未排序序列" 的第1个元素，小于 "已排序序列" 中的元素L[j] (j>=0表示没有超出 "未排序序列" 的下标范围)
            L[j+1] = L[j]  # 则将 "已排序序列" 中的元素L[j]的值复制给L[j+1]，相当于L[j]向后挪了一个位置
            j -= 1
        # 如果while条件为False：
        # 1. j < 0，则将 "未排序序列" 的第1个元素赋值给L[0]
        # 2. temp >= L[j]，则将 "未排序序列" 的第1个元素 "插入" 到L[j]的后面（自己尝试 i=4 时，就知道了）
        L[j+1] = temp


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
# Insertion sort function run 1,000,000 times, cost:  5.027623271 seconds.
