"""
方法一：排序

解题思路：
对原数组从小到大排序后取出前 k 个数即可

复杂度分析：
时间复杂度：O(nlogn)，其中 n 是数组 arr 的长度。算法的时间复杂度即排序的时间复杂度。
空间复杂度：O(logn)，排序所需额外的空间复杂度为 O(logn)。
"""


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]
