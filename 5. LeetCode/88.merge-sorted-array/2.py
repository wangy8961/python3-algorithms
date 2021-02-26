"""
方法二：双指针(i与j)，从前往后

解题思路：
nums1 有 m + n 的空间大小，可以用于储存最终的合并后的结果
需要额外的 m 大小的空间，将 nums1 前半段的原始数据(下标为 0 至 m-1)复制过去，比如叫 temp
现在相当于合并 temp 和 nums2 两个有序数组

1. 使用 i 和 j 分别指向 temp 和 nums2 开头元素
2. 比较 temp[i] 和 nums2[j] 的大小，将较小值存入结果数组 nums1 中
3. 依次类推直到 temp 或 nums2 其中一个序列为空时，再把另一个序列的剩余数据拷贝到 nums1 即可

复杂度分析：
时间复杂度：O(n+m)。
空间复杂度：O(m)。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]  # 额外的 m 大小的空间，保存 nums1 前半段的原始数据(下标为 0 至 m-1)

        i, j = 0, 0  # 分别表示 temp 和 nums2 数组中当前迭代的数据的下标
        k = 0  # 结果数组的下标，即较小值应该存放的位置
        while i < m and j < n:
            if temp[i] <= nums2[j]:  # 如果 temp 中的值较小时
                nums1[k] = temp[i]
                i += 1
            else:  # 如果 nums2 中的值较小时
                nums1[k] = nums2[j]
                j += 1

            k += 1  # 结果数组下标右移

        if i < m:  # temp 可能还有剩余的数据
            for p in range(i, m):
                nums1[k] = temp[p]
                k += 1
        if j < n:  # nums2 可能还有剩余的数据
            for q in range(j, n):
                nums1[k] = nums2[q]
                k += 1
