"""
方法二：堆排序

解题思路：
1. 将待排序的序列构建成一个大顶堆。此时，整个序列的最大值就是堆顶元素
2. 把堆顶元素跟底层数组的最后一个元素交换，那么下标为 n - 1 的元素就是整个序列的最大值
3. 然后再将剩余的 n - 1 个元素重新构建成一个大顶堆，这样就得到了 n 个元素中的第二大值。再把堆顶元素与底层数组中下标为 n - 2 的元素交换
4. 如此反复执行，就能得到一个有序序列了
"""


class Solution:
    def heapify(self, nums: List[int], start: int, end: int):  # 「迭代」
        """
        「自顶向下」进行堆化
        注意：除下标 start 节点以外，其它节点已经是一个大顶堆了！
        顺着该节点到叶子结点所在的路径，向下依次与它的左、右节点比较，如果左、右节点比它大，则交换它们

        假设存储堆的数组包含 n 个元素，下标从 0 到 n - 1
        堆其实是一颗完全二叉树，可以只对其中一个子树进行重新堆化，所以：
        start: 从哪个下标开始堆化，比如整棵树的根节点下标 0
        end: 到哪个下标结束堆化，比如 n (所有下标必须小于 n )
        """
        while True:
            larger = start  # 首先假设下标 start 的节点比它的左、右孩子节点大
            left = 2 * start + 1  # 下标 start 的节点的左孩子节点的下标
            right = 2 * start + 2  # 下标 start 的节点的右孩子节点的下标

            if left < end and nums[left] > nums[larger]:  # 如果左节点大，则 larger 更新为 left 下标
                larger = left
            if right < end and nums[right] > nums[larger]:  # 如果右节点更大，则 larger 更新为 right 下标
                larger = right

            if larger == start:  # 说明下标 start 的节点就是较大的，不需要交换。注意：此次循环前，下标 left 节点已经是以它为根的子树中最大的节点了；同理，下标 right 节点也已经是以它为根的子树中最大的节点了。所以，如果下标 start 节点比 left 和 right 都大，则无需继续向下探测，它已经是以它为根的子树中最大的节点了
                break
            else:
                nums[start], nums[larger] = nums[larger], nums[start]  # 交换
                start = larger  # 继续处理以下标 larger 为根节点的子树

    # def heapify(self, nums: List[int], start: int, end: int):  # 「递归」
    #     """
    #     「自顶向下」进行堆化
    #     注意：除下标 start 节点以外，其它节点已经是一个大顶堆了！
    #     顺着该节点到叶子结点所在的路径，向下依次与它的左、右节点比较，如果左、右节点比它大，则交换它们

    #     假设存储堆的数组包含 n 个元素，下标从 0 到 n - 1
    #     堆其实是一颗完全二叉树，可以只对其中一个子树进行重新堆化，所以：
    #     start: 从哪个下标开始堆化，比如整棵树的根节点下标 0
    #     end: 到哪个下标结束堆化，比如 n (所有下标必须小于 n )
    #     """
    #     larger = start  # 首先假设下标 start 的节点比它的左、右孩子节点大
    #     left = 2 * start + 1  # 下标 start 的节点的左孩子节点的下标
    #     right = 2 * start + 2  # 下标 start 的节点的右孩子节点的下标

    #     if left < end and nums[left] > nums[larger]:  # 如果左节点大，则 larger 更新为 left 下标
    #         larger = left
    #     if right < end and nums[right] > nums[larger]:  # 如果右节点更大，则 larger 更新为 right 下标
    #         larger = right

    #     if larger == start:  # 递归退出条件。说明下标 start 的节点就是较大的，不需要交换。注意：此次循环前，下标 left 节点已经是以它为根的子树中最大的节点了；同理，下标 right 节点也已经是以它为根的子树中最大的节点了。所以，如果下标 start 节点比 left 和 right 都大，则无需继续向下探测，它已经是以它为根的子树中最大的节点了
    #         return
    #     else:  # 说明下标 start 的节点不是较大的，需要交换它与 larger 的节点
    #         nums[start], nums[larger] = nums[larger], nums[start]  # 交换
    #         self._siftup(larger, end)  # 递归处理以下标 larger 为根节点的子树

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 1. 构建大顶堆：「原地堆化」调整 nums 数组，让其满足大顶堆的特性
        # 假设存储堆的数组 nums 从下标 0 开始计数，元素个数为 n。那么下标为 i 的元素的左孩子下标为 2i + 1，右孩子下标为 2i + 2
        # 「非叶子节点」的最大的下标为 n//2 - 1，所以我们只需要「自底向上、自右向左」依次针对每个非叶子节点进行「自顶向下」堆化，让其满足大顶堆的特性即可
        for i in reversed(range(n // 2)):  # 假设 nums = [30, 10, 50, 20, 90, 70]，则 i = [2, 1, 0]
            self.heapify(nums, i, n)  # 以每个「非叶子节点」为根节点，将其和其子树使用「自顶向下」进行堆化，调整成大顶堆

        # 2. 排序
        for i in range(n - 1, -1, -1):  # 下标 i 取值 [n-1, n-2, ... , 0]
            nums[0], nums[i] = nums[i], nums[0]  # 交换大顶堆的堆顶元素和数组的最后一个元素
            self.heapify(nums, 0, i)  # 对 nums[0:i] 子数组(只剩下 i 个元素，所以 heapify 函数的第三个参数为 i)重新进行堆化

        return nums
