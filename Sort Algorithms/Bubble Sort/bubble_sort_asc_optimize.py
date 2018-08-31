'''优化后的冒泡排序，升序'''
from timeit import timeit

def bubbLe_sort1(L):  # 优化前，最优时间复杂度和最坏时间复杂度都为O(n^2)
    n = len(L)
    for i in range(1, n):
        for j in range(n-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

def bubbLe_sort2(L):  # 优化后，最优时间复杂度为O(n)，最坏时间复杂度还是O(n^2)
    n = len(L)
    for i in range(1, n):
        count = 0
        for j in range(n-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                count += 1
        if not count:  # 如果我们在某一次冒泡操作中，内层遍历后发现没有交换任何元素位置，则说明此时列表已经是排序好了
            return


L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
L2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print('bubbLe_sort1 cost: ', timeit('bubbLe_sort1(L1)', 'from __main__ import bubbLe_sort1, L1'))
print('bubbLe_sort2 cost: ', timeit('bubbLe_sort2(L2)', 'from __main__ import bubbLe_sort2, L2'))

# Output:
# bubbLe_sort1 cost:  12.457272971  # timeit默认会执行100万次并返回平均运行时间，可以指定number=10000修改为运行1万次
# bubbLe_sort2 cost:  2.9928728069999995
