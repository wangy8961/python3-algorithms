"""
方法一: 堆

解题思路：
将多个链表的值读取到列表中，再使用 heapq.heapify() 构建为小顶堆，最后依次弹出堆顶元素构建结果链表即可
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 读取链表数组中所有节点的值
        h = []
        for node in lists:  # 多个链表的头节点组成的数组
            while node:  # 遍历其中一个有序链表
                h.append(node.val)
                node = node.next  # 指针后移

        if not h:  # 输入为 [] 或 [[]] 时
            return None

        # 构建小顶堆
        heapq.heapify(h)

        # 构建结果链表
        root = ListNode(heapq.heappop(h))
        cur = root
        while h:
            node = ListNode(heapq.heappop(h))  # 新节点
            cur.next = node  # 链表尾部添加新节点
            cur = node

        return root  # 返回结果链表的头节点
