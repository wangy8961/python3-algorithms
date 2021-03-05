"""
方法一：暴力枚举

解题思路：
枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配。
而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x。

复杂度分析：
时间复杂度：O(n^2)，其中 n 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次。
空间复杂度：O(1)。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
