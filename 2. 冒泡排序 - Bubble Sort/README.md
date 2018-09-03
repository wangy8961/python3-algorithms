# [> 算法概述](http://www.madmalls.com/blog/post/bubble-sort-algorithm/)

欢迎star， 并访问我的博客： www.madmalls.com


# 1. 算法介绍

`冒泡排序（Bubble Sort）`是一种简单的排序算法，它重复地遍历要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。遍历数列的工作会重复地进行，当不再有元素需要交换的时候，就表示数列排序完成了。`冒泡排序`与气泡上升的过程相似，气泡上升的过程中不断吸收空气而变大，`冒泡排序`算法也是依次比较相邻的两个元素，将较大的"浮"到最右边

![Bubble Sort 01](http://www.madmalls.com/admin/medias/uploaded/bubble-sort-01-04dbc2bc.gif)

算法（假设按升序排序）的主要步骤如下：

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
  ![Bubble Sort 02](http://www.madmalls.com/admin/medias/uploaded/bubble-sort-02-16b298ef.jpg)
  步骤1和步骤2合称为一次冒泡操作，上图演示了第1次冒泡操作，该冒泡操作需要进行`n-1`次比较。**每次冒泡操作会选出 "未排序序列" 的最大值，所以总共需要进行`n-1`次冒泡操作**
3. 针对所有的元素重复以上的步骤，除了最后一个（第2次冒泡操作，序列的最后一个元素是 "已排序序列"，该冒泡操作需要进行`n-2`次比较）
4. 持续对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较（冒泡操作只针对 "未排序序列"，所以每次冒泡操作的比较次数递减）


# 2. Python实现

假设要排序拥有 `n` 个元素的列表`L`，且按`升序`排列

## 2.1 错误的算法

下面的代码只是演示错误的情形，每次冒泡操作都遍历整个序列，将当前元素与 "已排序序列" 中的元素进行比较完全是浪费时间：

```python
from timeit import timeit


def bubbLe_sort(L):
    '''演示错误的冒泡算法'''
    n = len(L)
    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作都遍历整个列表的元素，即使后面已经排序好的元素也会比较，完全是在浪费时间
        for j in range(n-1):  # j 表示列表的下标，j不能取值n-1，否则L[j+1]会下标越界
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    print('Bubble sort function run 1,000,000 times, cost: ', timeit('bubbLe_sort(L2)', 'from __main__ import bubbLe_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Bubble sort function run 1,000,000 times, cost:  18.196879405 seconds.
```

## 2.2 正确的算法 

每次冒泡操作只针对 "未排序序列"，所以每次冒泡操作的比较次数递减：

| 冒泡操作次数 | 比较的次数 |
| ------------- | ---------------------- |
| 第1次，i = 0   | n-1                    |
| 第2次，i = 1 | n-2                    |
| 第3次，i = 2 | n-3                    |
| ...           | ...                    |
| 第n-1次，i = n-2 | 1                      |

> 助记：每次冒泡操作需要 `n-i-1` 次比较

```python
from timeit import timeit


def bubbLe_sort(L):
    '''冒泡排序，升序'''
    n = len(L)
    for i in range(n-1):  # 共需要n-1次冒泡操作

        # 每次冒泡操作，只遍历并比较 "未排序的序列" 中的元素（会依次变少）
        # 注意 j 表示序列的下标，所以 j 的取值范围为 0, 1, 2 ... n-i-2， 不能取n-i-1，否则后续L[j+1]会下标越界
        for j in range(n-i-1):  # 助记：每次冒泡操作需要 n-i-1 次比较
            if L[j] > L[j+1]:  # 如果L[j]比L[j+1]大，则交换它们的位置
                L[j], L[j+1] = L[j+1], L[j]


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    print('Bubble sort function run 1,000,000 times, cost: ', timeit('bubbLe_sort(L2)', 'from __main__ import bubbLe_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Bubble sort function run 1,000,000 times, cost:  12.419256763 seconds.
```

> 分析过程：

外层`for`循环中的变量`i`代表第几次冒泡操作，取值范围为`0, 1, 2 ... n-2`，对应`range(n-1)`。内层`for`循环中的变量`j`代表每次冒泡操作中的列表下标，因为每次冒泡操作中需要进行比较的列表元素范围会逐渐缩小，所以列表下标`j`的取值范围就应该不断变化：

1. 第1次冒泡操作，`i = 0`时，下标`j`的取值范围为`0, 1, 2 ... n-2`，因为要比较`L[j]`和`L[j+1]`的大小，所以`j`不能取`n-1`，否则`L[j+1]`将超出列表的下标范围（IndexError: list index out of range）
2. 第2次冒泡操作，`i = 1`时，下标`j`的取值范围为`0, 1, 2 ... n-3`，因为第1次冒泡操作过后，第`n`个元素（即`L[n-1]`）已经是列表的最大值，只需要对前`n-1`个元素进行冒泡操作即可
3. 第3次冒泡操作，`i = 2`时，下标`j`的取值范围为`0, 1, 2 ... n-4`

所以下标`j`的取值范围为`0, 1, 2 ... n-i-2`，对应`range(n-i-1)`

> 每一次冒泡操作后的状态图如下：

![Bubble Sort 03](http://www.madmalls.com/admin/medias/uploaded/bubble-sort-03-9155102c.jpg)

## 2.3 优化的算法

如果传入一个几乎已经按 "升序" 排列好的列表，章节2.2的代码还是会老老实实的执行两次完整的`for`循环，最优时间复杂度为`O(n^2)`。**如果我们在某一次冒泡操作中，内层遍历后发现没有交换任何元素位置，则说明此时列表已经是排序好了**：

![Bubble Sort 04](http://www.madmalls.com/admin/medias/uploaded/bubble-sort-04-adca27a4.jpg)

```python
from timeit import timeit


def bubbLe_sort(L):
    '''优化后的冒泡排序，升序
    最优时间复杂度为O(n)，比如L本身就是排好序的：[17, 20, 26, 31, 44, 54, 55, 77, 93]
    最坏时间复杂度还是O(n^2)
    '''
    n = len(L)
    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                flag = True
        if not flag:  # 如果我们在某一次冒泡操作中，内层遍历后发现没有交换任何元素位置，则说明此时列表已经是排序好了
            return


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    bubbLe_sort(L1)
    print('After: ', L1)

    print('Bubble sort function run 1,000,000 times, cost: ', timeit('bubbLe_sort(L2)', 'from __main__ import bubbLe_sort, L2'), 'seconds.')


# Output:
Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
Bubble sort function run 1,000,000 times, cost:  3.106356137 seconds.
```

# 3. 性能

## 3.1 时间复杂度

- 最优时间复杂度： `O(n)`，比如传入已经按 "升序" 排好序的列表时，章节2.3的代码首先会进行第1次外层循环，内层循环n-1次后，会结束算法，所以为`O(n)`
- 最坏时间复杂度： `O(n^2)`

## 3.2 空间复杂度

循环遍历时需要一个变量用作索引，并且需要一个临时变量来交换元素位置，所以空间复杂度为`O(1)`

## 3.3 稳定性

`冒泡算法`是比较相邻两元素的大小，如果他们的顺序错误就把他们交换过来，它是`稳定`的排序算法，比如传入 `[2, 2, 2, 1]`，按 "升序" 排序后，三个2总是维持原来的相对次序 `[1, 2, 2, 2]`
