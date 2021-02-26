"""
方法三：归并排序

解题思路：
「自底向上」使用迭代(iterative)的方式，实现归并排序算法
1. size = 1, 对仅包含单个元素的左右子序列进行合并操作
2. size = 2, 步骤1归并排序后，每2个元素已经是排序好的，所以可以对分别包含2个元素的左右子序列进行合并操作
3. size = 4, 步骤2归并排序后，每4个元素已经是排序好的，所以可以对分别包含4个元素的左右子序列进行合并操作
4. 如此反复执行，就能得到一个有序序列了
"""
from collections import deque


class Solution:
    def merge(self, left: int, right: int) -> List[int]:
        """使用双端队列 deque 简化左右子序列的合并操作"""
        merged, left, right = [], deque(left), deque(right)

        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)  # 合并左右子序列中剩余的还没有比较的元素

        return merged

    def merge_sort(self, nums: List[int]) -> List[int]:
        """不断计算出提供给合并函数 merge(left, right) 的左右子序列即可"""
        n = len(nums)
        size = 1  # size 表示要进行合并操作的左右子序列的长度，取值范围为 1, 2, 4 ... n-1。当 size = 1 时，左右子序列都是单个元素，肯定为有序的，可以直接合并操作了
        while size < n:  # size 最大值为 n - 1。如果 size < n-1，则序列为奇数个数时，最后一个元素不会被排序(错误!)
            low = 0  # low, mid, high 都表示下标
            while low + size < n:  # 保证 mid = low + size 不会下标越界
                mid = low + size
                high = mid + size  # 即 high = low + 2 * size

                left = nums[low:mid]
                right = nums[mid:high]  # 切片不会取high，所以 high = low + 2 * size 也没事

                merged = self.merge(left, right)  # 合并左右子序列

                nums[low:high] = merged  # 将合并操作排序好的序列，重新赋值给 nums[low:high]
                low = high  # 将下标 low 往右移动

            size = 2 * size  # 自底向上，第1次合并操作是针对单个元素，结果为2个元素。第2次合并操作就是针对2个元素，结果为4个元素...

        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
