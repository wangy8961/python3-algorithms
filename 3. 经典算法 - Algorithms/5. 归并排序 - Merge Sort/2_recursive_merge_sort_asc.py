from collections import deque


def merge_sort(L):
    '''使用 '递归(recursive)' 的方式，实现归并排序算法
    自顶向下(Top Down)
    '''
    n = len(L)
    # 两个作用：
    # 1. 客户端传入原始序列只有一个元素或为空时，不用排序，直接返回
    # 2. 递归的退出条件。如果传入的序列元素个数为1时，不再拆分，返回
    if n <= 1:
        return L

    # 将传入的序列拆分成左右两个子序列，再分别递归
    mid = n // 2
    left = merge_sort(L[:mid])  # 特别注意：先递归左边的，直到子序列元素为1个，才依次向上返回。比如L = [54, 26, 93, 17, 77, 31, 44, 55, 20]，则会先将 [54, 26, 93, 17] 归并排序好之后才会排右边的
    right = merge_sort(L[mid:])

    # 开始执行归并操作，将结果返回给上一层的 merge_sort() 调用栈
    return merge(left, right)


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

    def test():
        # import random
        # gen = (random.randint(1, 100) for i in range(100))  # 产生100个 1-99 范围内的随机整数
        # L = list(gen)
        L = [96, 2, 65, 23, 47, 58, 8, 48, 69, 92, 34, 83, 93, 47, 45, 55, 95, 15, 92, 24, 64, 19, 29, 55, 35, 48, 39, 29, 63, 94, 99, 38, 50, 10, 10, 93, 74, 27, 74, 44, 29, 81, 85, 86, 74, 30, 50, 50, 12, 12, 38, 75, 41, 87, 80, 97, 16, 48, 65, 69, 83, 71, 28, 9, 64, 69, 27, 74, 74, 86, 40, 69, 79, 79, 77, 100, 53, 72, 77, 16, 8, 36, 41, 58, 59, 29, 46, 79, 81, 66, 8, 35, 60, 52, 2, 82, 2, 36, 79, 66]
        merge_sort(L)

    def merge_sort(L):
        n = len(L)
        if n <= 1:
            return L

        mid = n // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])

        return merge(left, right)

    def merge(left, right):
        merged, left, right = [], deque(left), deque(right)

        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)

        return merged

    print('Merge sort function run 1000 times, cost: ', timeit('test()', 'from __main__ import test', number=1000), 'seconds.')


    # Output:
    # Merge sort function run 1000 times, cost:  0.4855265918162669 seconds.
    '''
