"""
方法三：双指针(i与j)，从后往前

解题思路：
nums1 有 m + n 的空间大小，可以用于储存最终的合并后的结果
从方法二借鉴下思路，我们可以依次比较 nums1 和 nums2 的较大者，保存到 nums1 的末尾即可

1. 使用 i 和 j 分别指向 nums1 和 nums2 的末尾元素(因为它们本来就是升序排列的)
2. 比较 nums1[i] 和 nums2[j] 的大小，将较大值存入结果数组 nums1 的末尾
3. 依次类推直到 nums1 前半段(下标为 0 至 m-1) 或 nums2 其中一个序列为空时，再把另一个序列的剩余数据依次往前拷贝到 nums1 即可

复杂度分析：
时间复杂度：O(n+m)。
空间复杂度：O(1)。
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1  # 分别表示 nums1 和 nums2 数组中当前迭代的数据的下标
        k = m + n - 1  # 结果数组的下标，即较大值应该存放的位置
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:  # 如果 nums1 中的值较大时
                nums1[k] = nums1[i]
                i -= 1
            else:  # 如果 nums2 中的值较大时
                nums1[k] = nums2[j]
                j -= 1

            k -= 1  # 结果数组下标左移

        # if i >= 0:  # nums1 可能还有剩余的数据。因为原始 nums1 就是有序的，所以剩余的下标 0 至 i 的元素还是有序的，且肯定比结果数组的小，所以无需再迭代复制！
        #     for p in range(i, -1, -1):
        #         nums1[k] = nums1[p]
        #         k -= 1
        if j >= 0:  # nums2 可能还有剩余的数据
            for q in range(j, -1, -1):
                nums1[k] = nums2[q]
                k -= 1
