# [> Python3数据结构与算法03 - 选择排序](http://www.madmalls.com/blog/post/selection-sort-algorithm/)

欢迎star， 并访问我的博客： www.madmalls.com



# 1. 算法介绍

`选择排序（Selection sort）`是一种简单直观的排序算法。它的工作原理如下：

1. 首先在`未排序序列`中找到最小（大）元素，存放到`已排序序列`的起始位置
2. 然后，再从剩余`未排序序列`中继续寻找最小（大）元素，然后放到`已排序序列`的末尾
3. 以此类推，直到所有元素均排序完毕

![Selection Sort 01](http://www.madmalls.com/admin/medias/uploaded/selection-sort-01-b5828ff6.gif)


# 2. Python实现

`选择排序`的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。`选择排序`每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对 `n` 个元素的序列进行排序总共进行至多 `n-1` 次交换。在所有的完全依靠交换去移动元素的排序方法中，`选择排序`属于非常好的一种：

![Selection Sort 02](http://www.madmalls.com/admin/medias/uploaded/selection-sort-02-3ead59ab.jpg)

```python
from timeit import timeit


def selection_sort(L):
    '''选择排序，升序'''
    n = len(L)
    for i in range(n-1):  # 共需要n-1次选择操作
        min_index = i  # 首先假设 "未排序列表"(上图中非绿色框) 的最小元素是它的第1个元素，第1次选择操作则假设L[0]是最小的，第2次操作则假设L[1]是最小的

        for j in range(i+1, n):  # 找出 "未排序列表" 中真正的最小元素的下标
            if L[j] < L[min_index]:
                min_index = j

        if min_index != i:  # 如果 "未排序列表" 中真正的最小元素，不是之前假设的元素，则进行交换
            L[i], L[min_index] = L[min_index], L[i]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    selection_sort(L1)
    print('After: ', L1)

    print('Selection sort function run 1,000,000 times, cost: ', timeit('selection_sort(L2)', 'from __main__ import selection_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Selection sort function run 1,000,000 times, cost:  10.988781472000001 seconds.
```

# 3. 性能

## 3.1 时间复杂度

### (1) 最优时间复杂度: `O(n^2)`

### (2) 平均时间复杂度: `O(n^2)`

![selection sort 03](http://www.madmalls.com/admin/medias/uploaded/selection-sort-03-17dd63a9.gif)

### (3) 最坏时间复杂度: `O(n^2)`

比如传入已经按 "降序" 排好序的列表，却需要按 "升序" 去排列它

![selection sort 04](http://www.madmalls.com/admin/medias/uploaded/selection-sort-04-e4722bb8.gif)


## 3.2 空间复杂度

循环遍历时需要一个变量用作索引，并且需要一个临时变量来交换元素位置，所以空间复杂度为`O(1)`

## 3.3 稳定性

`选择排序`是`不稳定`排序算法：

![Selection sort 05](http://www.madmalls.com/admin/medias/uploaded/selection-sort-05-dbfcba44.jpg)
