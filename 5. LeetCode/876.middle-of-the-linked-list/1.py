"""
方法一: 数组

解题思路：
链表的缺点在于不能通过下标访问对应的节点。
因此我们可以考虑对链表进行遍历，同时将遍历到的节点依次放入数组 arr 中。
如果我们遍历到了 n 个节点，那么链表以及数组的长度也为 n，对应的中间节点即为 arr[n//2]。

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。
空间复杂度：O(n)。数组 arr 占用的空间
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []  # 使用数组存储遍历到的链表节点，方便后续通过数组的按下标随机访问的特性，直接返回中间节点
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        return arr[len(arr) // 2]
