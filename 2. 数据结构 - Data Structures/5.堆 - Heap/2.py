"""
Python 语言中的 heapq 模块创建的是小顶堆，因此我们可以对待排序的序列中所有的数取反，就相当于维护了大顶堆
我们这里使用数组来存储堆中元素，实现一个简单的大顶堆，支持插入元素(heappush)，弹出堆顶元素(heappop)，更新堆顶元素(heapreplace)，原地堆化数组(heapify)

注意：「堆化」操作只针对原来就是有效堆结构，当堆顶元素改变了(_siftdown)、或者在堆尾添加了新元素(_siftup)时，才能调用这两个堆化函数！
分为从上往下和从下往上堆化，因为单个元素的变化所以需要调整结构，让其继续符合大顶堆的特性，将较大的元素依次交换到父节点，堆顶元素是最大的
"""
from typing import List


class MaxHeap:
    def __init__(self, nums: List[int] = None, capacity: int = 128) -> None:
        self.heap = []  # 使用数组来存储堆中元素
        self.capacity = capacity  # 堆可以存储的最大数据个数

        if isinstance(nums, list):
            self.heapify(nums)

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def heappush(self, item):
        """把新插入的元素添加到堆的最后，再重新堆化"""
        if len(self.heap) == 0:  # 空堆
            self.heap.append(item)
            return
        if len(self.heap) >= self.capacity:  # 堆已经满了
            raise ValueError(f"The heap structure has reached the maximum capacity of {self.capacity}")
        self.heap.append(item)  # 在底层数组末尾添加元素，时间复杂度为 O(1)
        # 自底向上进行堆化，与完全二叉树的高度相关，时间复杂度为 O(logn)
        self._siftup(len(self.heap) - 1, 0)

    def heappop(self):
        """删除堆顶元素
        如果直接删除堆顶元素，就需要把第二大的元素(肯定在它的左、右节点中)放到堆顶。然后再迭代地删除第二大节点，以此类推，直到叶子节点被删除。这种方法有点问题，就是最后堆化出来可能出现数据空洞，就会不满足完全二叉树的特性

        正确方法：
        1. 先把堆顶元素保存到临时变量中，用于最后返回
        2. 删除堆的最后一个元素，并将它的值更新为新的堆顶元素
        3. 对新堆顶元素，使用「自顶向下」进行堆化。将它与左、右节点比较大小，如果左节点或右节点比它大，则交换它们
        4. 以此类推，直到父子节点不再需要交换
        """
        if len(self.heap) == 0:  # 空堆
            raise ValueError("The heap structure has no element")
        root = self.heap[0]  # 原堆顶元素，最后需要返回给用户
        last_item = self.heap.pop()  # 删除堆的最后一个元素。在底层数组末尾删除元素，时间复杂度为 O(1)
        self.heap[0] = last_item  # 并将它的值更新为新的堆顶元素
        self._siftdown(0, len(self.heap))  # 自顶向下进行堆化
        return root

    def heapreplace(self, item):
        """弹出堆顶元素，并添加新插入的元素，重新堆化
        注意：如果先 heappop() 再 heappush()，需要两次堆化，会增加比较和交换的次数，不推荐！
        """
        if len(self.heap) == 0:  # 空堆
            self.heap.append(item)
            return
        root = self.heap[0]  # 原堆顶元素，最后需要返回给用户
        self.heap[0] = item  # 并将新插入的元素更新为新的堆顶元素
        self._siftdown(0, len(self.heap))  # 自顶向下进行堆化
        return root

    def heapify(self, nums: List[int]) -> None:
        """堆化：「原地」调整 nums 数组，让其满足大顶堆的特性
        假设存储堆的数组 nums 从下标 0 开始计数，元素个数为 n。那么下标为 i 的元素的左孩子下标为 2i + 1，右孩子下标为 2i + 2
        「非叶子节点」的最大的下标为 n//2 - 1，所以我们只需要「自底向上、自右向左」依次针对每个非叶子节点进行「自顶向下」堆化，让其满足大顶堆的特性即可
        """
        self.heap = nums
        n = len(nums)
        for i in reversed(range(n // 2)):  # 假设 nums = [30, 10, 50, 20, 90, 70]，则 i = [2, 1, 0]
            self._siftdown(i, n)  # 以每个「非叶子节点」为根节点，将其和其子树使用「自顶向下」进行堆化，调整成大顶堆

    def _siftup(self, start: int, end: int):
        """
        「自底向上」进行堆化
        注意：除下标 start 节点以外，其它节点已经是一个大顶堆了！
        顺着该节点到根节点所在的路径，向上依次与父节点比较，如果它比父节点大，则交换它们

        假设存储堆的数组包含 n 个元素，下标从 0 到 n - 1
        start: 从哪个下标(新插入的节点的下标)开始堆化，比如 n - 1
        end: 到哪个下标结束堆化，比如整棵树的根节点下标 0
        """
        # Follow the path to the root, moving parents down until finding a place new item fits.
        while start > end:
            parent = (start - 1) // 2  # 父节点的下标
            if self.heap[start] > self.heap[parent]:  # 如果新插入的节点比父节点大，则交换它们
                self.heap[start], self.heap[parent] = self.heap[parent], self.heap[start]
                start = parent
            else:  # 不用再向上比较了，上面的祖父节点都比父节点大
                break

    def _siftdown(self, start: int, end: int):  # 「迭代」
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

            if left < end and self.heap[left] > self.heap[larger]:  # 如果左节点大，则 larger 更新为 left 下标
                larger = left
            if right < end and self.heap[right] > self.heap[larger]:  # 如果右节点更大，则 larger 更新为 right 下标
                larger = right

            if larger == start:  # 说明下标 start 的节点就是较大的，不需要交换。注意：此次循环前，下标 left 节点已经是以它为根的子树中最大的节点了；同理，下标 right 节点也已经是以它为根的子树中最大的节点了。所以，如果下标 start 节点比 left 和 right 都大，则无需继续向下探测，它已经是以它为根的子树中最大的节点了
                break
            else:
                self.heap[start], self.heap[larger] = self.heap[larger], self.heap[start]  # 交换
                start = larger  # 继续处理以下标 larger 为根节点的子树

    # def _siftdown(self, start: int, end: int):  # 「递归」
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

    #     if left < end and self.heap[left] > self.heap[larger]:  # 如果左节点大，则 larger 更新为 left 下标
    #         larger = left
    #     if right < end and self.heap[right] > self.heap[larger]:  # 如果右节点更大，则 larger 更新为 right 下标
    #         larger = right

    #     if larger == start:  # 递归退出条件。说明下标 start 的节点就是较大的，不需要交换。注意：此次循环前，下标 left 节点已经是以它为根的子树中最大的节点了；同理，下标 right 节点也已经是以它为根的子树中最大的节点了。所以，如果下标 start 节点比 left 和 right 都大，则无需继续向下探测，它已经是以它为根的子树中最大的节点了
    #         return
    #     else:  # 说明下标 start 的节点不是较大的，需要交换它与 larger 的节点
    #         self.heap[start], self.heap[larger] = self.heap[larger], self.heap[start]  # 交换
    #         self._siftup(larger, end)  # 递归处理以下标 larger 为根节点的子树


if __name__ == '__main__':
    nums = [30, 10, 50, 20, 90, 70]
    heap = MaxHeap(nums=nums)
    print(heap)

    print('*' * 50)
    heap.heappush(40)
    heap.heappush(60)
    heap.heappush(80)
    print(heap)

    print('*' * 50)
    top = heap.heappop()
    print(f'top: {top}')
    print(heap)
