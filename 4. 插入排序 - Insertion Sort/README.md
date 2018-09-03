# [> Python3数据结构与算法04 - 插入排序](http://www.madmalls.com/blog/post/insertion-sort-algorithm/)

欢迎star， 并访问我的博客： www.madmalls.com



# 1. 算法介绍

`插入排序（Insertion Sort）`是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于`未排序序列`中的某个数据，在`已排序序列`中从后向前扫描，找到相应位置并插入。`插入排序`在实现上，通常采用in-place排序（即只需用到`O(1)`的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间

1. 将初始未排序序列的第1个元素当作一个`已排序序列`，把第2个元素到最后一个元素当作`未排序序列`
2. 从头到尾依次扫描`未排序序列`，将扫描到的每个元素插入`已排序序列`的适当位置（从后向前扫描`已排序序列`）。如果待插入的元素与`已排序序列`中的某个元素相等，则将待插入的元素插入到相等元素的后面

![Insertion Sort 01](http://www.madmalls.com/admin/medias/uploaded/insertion-sort-b0a171ee.gif)

# 2. Python实现

![Insertion Sort 02](http://www.madmalls.com/admin/medias/uploaded/insertion-sort-02-a2ca567e.jpg)

## 2.1 算法1

相当于将 L[i] 与 "已排序序列" 中的元素（从后向前）依次比较，如果 L[i] 比较小，则交换位置：

```python
from timeit import timeit


def insertion_sort(L):
    '''插入排序，升序'''
    n = len(L)
    if n == 1:
        return

    # 首先，假设第1个元素L[0]是 "已排序序列"，第2个元素L[1]至最后一个元素L[n-1]是 "未排序序列"
    for i in range(1, n):  # 共需要 n-1 次插入操作。 i 表示 "未排序序列" 的第1个元素的下标，所以 i 从下标 1 开始

        # j 的范围是 [i, i-1，... 2, 1]，即包含下标 i 和 "已排序序列" 的所有下标
        for j in range(i, 0, -1):  # 将 "未排序序列" 的第1个元素L[i]，依次与 "已排序序列" 中的所有元素比较
            if L[j] < L[j-1]:  # 如果小于前一个元素，则交换位置
                L[j], L[j-1] = L[j-1], L[j]
            else:  # 如果不小于前一个元素，则肯定不小于这个元素之前的所有元素（因为前面已排好序了），所以可以退出比较的循环
                break


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    print('Insertion sort function run 1,000,000 times, cost: ', timeit('insertion_sort(L2)', 'from __main__ import insertion_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Insertion sort function run 1,000,000 times, cost:  7.045618813 seconds.
```

## 2.2 算法2

相当于将 L[i] 提起来，再与 "已排序序列" 中的元素（从后向前）依次比较，如果 L[i] 比较小，则将 "已排序序列" 中的元素依次往后挪一个位置：

```python
from timeit import timeit


def insertion_sort(L):
    '''插入排序，升序'''
    n = len(L)
    if n == 1:
        return

    for i in range(1, n):
        temp = L[i]  # 右手抓到一张扑克牌
        j = i - 1  # 拿在左手上的牌总是排序好的
        while j >= 0 and temp < L[j]:  # 将抓到的牌与左手上的牌（从右向左）进行比较
            L[j+1] = L[j]  # 如果左手上的牌比右手抓到的牌大，就将其右移
            j -= 1
        # 如果while条件为False：
        # 1. j < 0，左手上的牌都比右手抓到的牌小，则将抓到的牌插到左手第1张的前面
        # 2. temp >= L[j]，左手上的某张牌比右手抓到的牌小（或相等），则将抓到的牌插到左手这张牌的后面（相等元素的相对次序不会该变，所以该算法是稳定的）
        L[j+1] = temp


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    print('Insertion sort function run 1,000,000 times, cost: ', timeit('insertion_sort(L2)', 'from __main__ import insertion_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Insertion sort function run 1,000,000 times, cost:  5.027623271 seconds.
```

# 3. 性能

## 3.1 时间复杂度

- 最优时间复杂度： `O(n)`，比如传入已经按 "升序" 排好序的列表，上述代码按 "升序" 去排列它
- 最坏时间复杂度： `O(n^2)`

## 3.2 空间复杂度

循环遍历时需要一个变量用作索引，并且需要一个临时变量来交换元素位置，所以空间复杂度为`O(1)`

## 3.3 稳定性

`选择排序`是`稳定`的排序算法
