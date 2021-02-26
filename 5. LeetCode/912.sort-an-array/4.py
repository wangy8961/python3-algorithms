"""
方法四：归并排序(优化版)
https://www.geeksforgeeks.org/iterative-merge-sort/

解题思路：
「自底向上」使用迭代(iterative)的方式，实现归并排序算法
1. size = 1, 对仅包含单个元素的左右子序列进行合并操作
2. size = 2, 步骤1归并排序后，每2个元素已经是排序好的，所以可以对分别包含2个元素的左右子序列进行合并操作
3. size = 4, 步骤2归并排序后，每4个元素已经是排序好的，所以可以对分别包含4个元素的左右子序列进行合并操作
4. 如此反复执行，就能得到一个有序序列了
"""


class Solution:
    def merge(self, nums: List[int], low: int, mid: int, high: int):
        """合并左右两个「有序」子数组
        左子数组 arr1 下标 low 至 mid
        右子数组 arr2 下标 mid + 1 至 high
        """
        temp = []  # 临时结果数组，大小为 high - low + 1
        i, j = low, mid + 1  # 分别表示 arr1 和 arr2 数组中当前迭代的数据的下标

        while i <= mid and j <= high:
            if nums[i] <= nums[j]:  # 如果 arr1 中的值较小时
                temp.append(nums[i])
                i += 1
            else:  # 如果 arr2 中的值较小时
                temp.append(nums[j])
                j += 1

        if i <= mid:  # arr1 可能还有剩余的数据
            for p in range(i, mid + 1):
                temp.append(nums[p])
        if j <= high:  # arr2 可能还有剩余的数据
            for q in range(j, high + 1):
                temp.append(nums[q])

        # 将临时结果数组复制到原始数组中指定区域。不要使用切片操作：nums[low:high+1] = temp
        for k in range(high - low + 1):
            nums[low + k] = temp[k]

    def merge_sort(self, nums: List[int]) -> List[int]:
        """不断计算出提供给合并函数 merge() 的左右子序列的下标即可"""
        n = len(nums)
        size = 1  # size 表示要进行合并操作的左右子序列的长度，取值范围为 1, 2, 4, 8 ... n/2。当 size = 1 时，左右子序列都是单个元素，肯定为有序的，可以直接合并操作了
        while size <= n - 1:  # 如果 size < n-1，则序列为奇数个数时，最后一个元素不会被排序(错误!)
            low = 0  # low, mid, high 都表示下标
            while low < n - 1:  # 理想情况下是左右子序列两两合并，但是也可能存在剩余一个左子序列没人跟它合并，直到最后一次 merge 操作
                mid = min(low + size - 1, n - 1)
                high = min(low + 2 * size - 1, n - 1)

                self.merge(nums, low, mid, high)  # 合并左子序列(arr[low...mid])和右子序列(arr[mid+1...high])
                low += 2 * size  # 将下标 low 往右移动

            size = 2 * size  # 自底向上，第1次合并操作是针对单个元素，结果为2个元素。第2次合并操作就是针对2个元素，结果为4个元素...

    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums)
        return nums
