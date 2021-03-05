"""
方法二：哈希表

解题思路：
创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，
如果不存在就将 x 和对应的下标插入到哈希表中，即可保证不会让 x 和自己匹配

复杂度分析：
时间复杂度：O(n)，其中 n 是数组中的元素数量。对于每一个元素 x，我们可以 O(1) 地寻找 target - x。
空间复杂度：O(n)，主要为哈希表的开销。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # 哈希表
        for i, x in enumerate(nums):
            if target - x in d:
                return [d[target - x], i]
            d[x] = i
        return []
