'''插入排序，升序'''

def insert_sort(L):
    n = len(L)
    # 首先，假设第1个元素L[0]是 "已排序序列"，第2个元素L[1]至最后一个元素L[n-1]是 "未排序序列"
    for i in range(1, n):  # 共需要 n-1 次插入操作。 i 表示 "未排序序列" 的第1个元素的下标，所以 i 从下标 1 开始

        # j 的范围是 [i, i-1，... 2, 1]，即包含下标 i 和 "已排序序列" 的所有下标
        for j in range(i, 0, -1):  # 将 "未排序序列" 的第1个元素L[i]，依次与 "已排序序列" 中的所有元素比较
            if L[j] < L[j-1]:  # 如果小于前一个元素，则交换位置
                L[j], L[j-1] = L[j-1], L[j]

L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('Before: ', L1)
insert_sort(L1)
print('After: ', L1)

# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]