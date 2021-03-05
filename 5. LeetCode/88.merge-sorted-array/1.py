"""
方法一：合并后排序

解题思路：
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = sorted(nums1[:m] + nums2)

上面的解法使用了列表切片、列表相加、sorted()内建函数都会产生新的列表对象，所以空间复杂度不是 O(1)，不推荐！

list.sort() 函数是原地排序：
sort(self, /, *, key=None, reverse=False)
    Sort the list in ascending order and return None.

    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).

因此，我们可以将 nums2 中的数据依次复制到 nums1 的后半段(下标为 m 至 m+n-1)，再借助于 list.sort() 进行原地排序

复杂度分析：
时间复杂度：O((n+m) * log(n+m))。
空间复杂度：O(log(n+m))。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):  # 将 nums2 中的数据依次复制到 nums1 的后半段(下标为 m 至 m+n-1)
            nums1[m + i] = nums2[i]
        nums1.sort()  # list 原地排序
