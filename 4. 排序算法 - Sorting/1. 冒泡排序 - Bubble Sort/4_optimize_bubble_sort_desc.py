def bubbLe_sort(L):
    '''优化后的冒泡排序，降序
    最优时间复杂度为O(n)，比如L本身就是排好序的：[93, 77, 55, 54, 44, 31, 26, 20, 17]
    最坏时间复杂度还是O(n^2)
    '''
    n = len(L)
    if n <= 1:
        return

    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                flag = True
        if not flag:  # 如果我们在某一次冒泡操作中，内层遍历后发现没有交换任何元素位置，则说明此时列表已经是排序好了
            return


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
