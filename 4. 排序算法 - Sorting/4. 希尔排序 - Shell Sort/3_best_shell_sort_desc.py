from gaps import sedgewick_gaps


def shell_sort(L):
    '''希尔排序，降序'''
    n = len(L)
    if n <= 1:
        return

    gen = sedgewick_gaps(n)  # [1, 5, 19, 41, 109, 209, 505, 929 ...]
    for gap in reversed(list(gen)):  # 将gen生成器对象转换成列表，再倒序: [41, 19, 5, 1]

        # 想像成，以步长 gap 将原始序列划分成 gap 个待排序的序列，对每个序列使用普通的插入排序进行排序
        # 序列1: [L[0], L[gap], L[2*gap]...]
        # 序列2: [L[1], L[1+gap], L[1 + 2*gap]...]
        # 序列3: [L[2], L[2+gap], L[2 + 2*gap]...]
        # 请查看插入排序算法 https://github.com/wangy8961/python3-algorithms/blob/master/4.%20%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F%20-%20Insertion%20Sort/3_best_insertion_sort_asc.py
        # 助记：普通的插入排序算法中步长是 1 ，把插入排序中的步长 1 替换为 gap
        for i in range(gap, n):  # "未排序序列" 的第1个元素分别是L[gap], L[1+gap], L[2+gap] ... ，所以变量 i 表示的下标是 gap, 1+gap, 2+gap ...
            temp = L[i]
            j = i
            # j >= gap是因为后续j[j-gap]，否则下标越界
            while j >= gap and temp > L[j-gap]:
                L[j] = L[j-gap]
                j -= gap
            L[j] = temp


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    shell_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
