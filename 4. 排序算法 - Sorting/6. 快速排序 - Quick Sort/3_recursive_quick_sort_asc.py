def quick_sort(L, first, last):
    '''使用 '递归(recursive)' 的方式，实现快速排序算法
    first 和 last 都表示序列的下标
    '''
    if first < last:
        pivot_index = partition(L, first, last)  # 返回 '基准' 值的最终正确位置的下标
        quick_sort(L, first, pivot_index-1)
        quick_sort(L, pivot_index+1, last)


def partition(L, first, last):
    '''一次快速排序的分区过程，将选定的 '基准(pivot)' 放到正确的位置上，小于它的值都在它的左边，大于它的值都在它的右边
    first 和 last 都表示序列的下标
    '''
    smaller_index = first - 1  # index of smaller element (the last smaller element)
    pivot_value = L[last]  # takes last element as pivot

    for i in range(first, last):
        # If current element is smaller than or equal to pivot
        if L[i] <= pivot_value:
            # increment index of smaller element
            smaller_index += 1
            L[smaller_index], L[i] = L[i], L[smaller_index]

    # places the pivot element at its correct position (behind the last smaller element)
    L[smaller_index + 1], L[last] = L[last], L[smaller_index + 1]
    return smaller_index + 1  # return the index of pivot element


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    quick_sort(L1, 0, len(L1)-1)
    print('After: ', L1)

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
        quick_sort(L, 0, len(L)-1)

    def quick_sort(L, first, last):
        if first < last:
            pivot_index = partition(L, first, last)
            quick_sort(L, first, pivot_index-1)
            quick_sort(L, pivot_index+1, last)


    def partition(L, first, last):
        smaller_index = first - 1
        pivot_value = L[last]

        for i in range(first, last):
            if L[i] <= pivot_value:
                smaller_index += 1
                L[smaller_index], L[i] = L[i], L[smaller_index]

        L[smaller_index + 1], L[last] = L[last], L[smaller_index + 1]
        return smaller_index + 1


    print('Quick sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')


    # Output:
    # Quick sort function run 1000 times, cost:  0.2604488975027085 seconds.
    '''
