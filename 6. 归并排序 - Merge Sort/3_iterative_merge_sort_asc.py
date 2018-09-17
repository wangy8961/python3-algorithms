from collections import deque


def merge_sort(L):
    '''使用 迭代(iterative) 的方式，实现归并排序算法
    自底向上(Bottom Up)：
    1. size = 1, 对单个元素的左右子序列进行归并操作
    2. size = 2, 步骤1归并排序后，每2个元素已经是排序好的，所以可以对分别包含2个元素的左右子序列进行归并操作
    3. size = 4, 步骤2归并排序后，每4个元素已经是排序好的，所以可以对分别包含4个元素的左右子序列进行归并操作
    ...
    '''
    n = len(L)
    # size表示要进行归并操作的左右子序列的长度，取值范围为1, 2, 4 ... n-1
    size = 1  # 当 size = 1 时，左右子序列都是单个元素，肯定为有序的，可以直接归并操作了
    while size < n:  # size最大值为 n - 1； 如果size < n-1，则序列为奇数个数时，最后一个元素不会被排序，是错误的
        '''提供 left 和 right 两个子序列给 merge(left, right) 函数即可'''
        # low, mid, high 都表示下标
        low = 0
        while low + size < n:  # 保证 mid = low + size 不会下标越界
            mid = low + size
            high = mid + size  # 即 high = low + 2 * size

            left = L[low:mid]
            right = L[mid:high]  # 切片不会取high，所以 high = low + 2 * size 也没事

            merged = merge(left, right)
            # 将归并操作排序好的序列，重新赋值给 L[low:high]
            L[low:high] = merged
            # 将下标 low 往右移动
            low = high
        # 自底向上，第1次归并操作是针对单个元素，结果为2个元素。第2次归并操作就是针对2个元素，结果为4个元素...
        size = 2 * size

    return L


def merge(left, right):
    '''归并操作，使用deque'''
    merged, left, right = [], deque(left), deque(right)

    while left and right:
        merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
    merged.extend(right if right else left)  # 如果 left序列 还有没比较的元素

    return merged


def is_sorted(L):
    '''辅助函数: 用来判断 '归并排序函数(merge_sort)' 的输出结果是否是正确的升序序列'''
    prev = L[0]
    for i in range(1, len(L)):
        if prev > L[i]:
            print('Sort ascending failed.')
            return False
        prev = L[i]
    print('Sort ascending succeed.')
    return True


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    merged = merge_sort(L1)
    if is_sorted(merged):
        print('After: ', merged)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # Sort ascending succeed.
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]

    '''
    压力测试，timeit.timeit() 如果from __main__ import L，结果好像不对，所以在函数内初始化相同的L：

    from collections import deque
    from timeit import timeit

    def merge_sort():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]

        n = len(L)
        size = 1
        while size < n:
            low = 0
            while low + size < n:
                mid = low + size
                high = mid + size

                left = L[low:mid]
                right = L[mid:high]

                merged = merge(left, right)
                L[low:high] = merged

                low = high

            size = 2 * size

        return L

    def merge(left, right):
        merged, left, right = [], deque(left), deque(right)

        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)

        return merged


    print('Merge sort function run 1000 times, cost: ', timeit('merge_sort()', 'from __main__ import merge_sort', number=1000), 'seconds.')


    # Output:
    # Merge sort function run 1000 times, cost:  0.5063995326536888 seconds.
    '''
