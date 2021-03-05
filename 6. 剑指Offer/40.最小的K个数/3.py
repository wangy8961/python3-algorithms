"""
方法三：快排
"""

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        self.quick_sort(arr, 0, len(arr) - 1, k)
        return arr[:k]

    def quick_sort(self, arr: List[int], low: int, high: int, k: int) -> None:
        mid = self.partition(arr, low, high)
        size = mid - low + 1  # 分区后，「左边分区 + pivot」的元素个数
        if k == size:  # 递归退出条件，已经找到了前 k 个最小的元素
            return
        elif k < size:  # k 个最小的元素只占了左边分区的一部分，所以递归对左边分区继续进行分区操作
            self.quick_sort(arr, low, mid - 1, k)
        else:  # 还有 k - size 个元素在右边分区，所以递归对右边分区继续进行分区操作
            self.quick_sort(arr, mid + 1, high, k - size)

    def partition(self, arr: List[int], low: int, high: int) -> int:
        """分区操作：将小于或等于基准值的元素放在基准的左边，将大于基准值的元素放在基准的右边，基准处于数列的中间位置，
        返回基准元素 pivot 的下标"""
        pivot = arr[high]  # 假设选择最后一个元素作为基准元素pivot
        """
        import random
        pivot_index = random.randint(low, high)  # 采用随机的方式选择pivot
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # 再将pivot放到末尾
        """

        i = low - 1  # i 表示「小于或等于pivot的区间」的元素下标
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1  # 「小于或等于pivot的区间」元素个数增加了
                arr[i], arr[j] = arr[j], arr[i]  # 将 arr[j] 插入「小于或等于pivot的区间」的末尾，使用交换两个元素值的方法可以省去数组数据搬移

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 「小于或等于pivot的区间」后面的元素应该是基准元素应该在的位置！所以将pivot交换到正确的位置，此时它的新下标 i + 1 就是 partition() 的返回值
        return i + 1
