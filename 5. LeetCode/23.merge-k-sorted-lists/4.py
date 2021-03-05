"""
方法四: 堆

解题思路：
将多个链表的值读取到列表中，再使用 heapq.heapify() 构建为小顶堆，最后依次弹出堆顶元素构建结果链表即可

复杂度分析：
时间复杂度：O(kn * log(kn))。假设每个链表的最长的长度是 n。堆中元素为 k * n 个，插入和删除操作为 O(log(kn))，每个节点值都被插入和删除一次，故总的时间复杂度为 O(kn * log(kn))
空间复杂度：O(kn) or O(?)。堆中最多元素个数为 kn，空间复杂度为 O(kn)，而且还会根据 val 重建全部链表节点
"""
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 读取 lists 中 k 个有序链表的所有节点的值
        h = []
        for node in lists:  # node 表示某个有序链表的第一个节点
            while node:  # 遍历此有序链表
                h.append(node.val)
                node = node.next  # 指针后移

        if not h:  # 输入为 [] 或 [[]] 时
            return None

        # 构建小顶堆，问题是根据 val 构建的小顶堆，无法对应原链表的节点
        heapq.heapify(h)

        # 构建结果链表
        head = ListNode(heapq.heappop(h))  # 根据 val 创建了新节点，空间消耗大，而且实际开发中需要保持链表中的原始节点不变(id不变、内存地址不变)
        cur = head
        while h:
            node = ListNode(heapq.heappop(h))  # 根据 val 创建了新节点，空间消耗大，而且实际开发中需要保持链表中的原始节点不变(id不变、内存地址不变)
            cur.next = node  # 链表尾部添加新节点
            cur = node

        return head
