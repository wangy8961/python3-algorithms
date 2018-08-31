'''冒泡排序，降序'''

def bubbLe_sort(L):
    n = len(L)
    for i in range(1, n):  # 共需要n-1次冒泡操作
        for j in range(n-i):  # 每次冒泡操作中的比较次数不同
            if L[j] < L[j+1]:  # 如果L[j]比L[j+1]小，则交换它们的位置
                L[j], L[j+1] = L[j+1], L[j]


L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('Before: ', L1)
bubbLe_sort(L1)
print('After: ', L1)

# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
