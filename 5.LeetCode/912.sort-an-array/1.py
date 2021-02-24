"""
方法一：快排

解题思路：
快速排序通过设计巧妙的原地分区函数，可以实现原地排序，解决了归并排序占用太多内存的问题
"""


class Solution:
    def partition(self, nums: List[int], low: int, high: int) -> int:
        """分区操作：将小于或等于基准值的元素放在基准的左边，将大于基准值的元素放在基准的右边，基准处于数列的中间位置，
        返回基准元素 pivot 的下标"""
        pivot = nums[high]  # 假设选择最后一个元素作为基准元素pivot
        """
        import random
        pivot_index = random.randint(low, high)  # 采用随机的方式选择pivot
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]  # 再将pivot放到末尾
        """

        i = low - 1  # i 表示「小于或等于pivot的区间」的元素下标
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1  # 「小于或等于pivot的区间」元素个数增加了
                nums[i], nums[j] = nums[j], nums[i]  # 将 nums[j] 插入「小于或等于pivot的区间」的末尾，使用交换两个元素值的方法可以省去数组数据搬移

        nums[i + 1], nums[high] = nums[high], nums[i + 1]  # 「小于或等于pivot的区间」后面的元素应该是基准元素应该在的位置！所以将pivot交换到正确的位置，此时它的新下标 i + 1 就是 partition() 的返回值
        return i + 1

    def quick_sort(self, nums: List[int], low: int, high: int) -> None:
        if low >= high:  # 递归退出条件
            return
        mid = self.partition(nums, low, high)  # 返回基准元素 pivot 的下标
        self.quick_sort(nums, low, mid - 1)  # 对左边区间递归的快排
        self.quick_sort(nums, mid + 1, high)  # 对右边区间递归的快排

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
