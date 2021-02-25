"""
方法六: 优先级队列 queue.PriorityQueue

解题思路：
堆也叫优先级队列，这里参考方法五，但是使用内建的 queue.PriorityQueue 来实现

复杂度分析：
时间复杂度：考虑队列中元素不超过 k 个，那么插入和删除的时间代价为 O(logk)，这里最多有 kn 个节点，对于每个节点都被插入和删除各一次，故总的时间代价即渐进时间复杂度为 O(kn * logk)
空间复杂度：队列中元素不超过 k 个，故渐进空间复杂度为 O(k)。
"""
from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class QueueNode:
    def __init__(self, node: ListNode):
        self.val = node.val
        self.node = node

    # 重载小于比较
    def __lt__(self, other):
        return self.val < other.val

    # 重载等于比较
    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 创建优先级队列
        que = PriorityQueue()

        # 读取 lists 中 k 个有序链表的第一个节点，创建为 QueueNode 类的实例对象(对象中引用了链表节点，不存在新建操作，内存消耗小)
        for node in lists:
            if node:  # 排除 [[]] 或 [[], [1,3], [2,6]] 这种情况，此时 node = []
                que.put(QueueNode(node))  # 入队

        # 构建结果链表
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」

        while not que.empty():  # 直到优先级队列为空
            v = que.get()  # 优先级最小的先出队

            tail.next = v.node  # tail 指向 v.node 节点
            tail = tail.next  # tail 指针后移

            if v.node.next is not None:
                que.put(QueueNode(v.node.next))  # 入队

        return root.next
