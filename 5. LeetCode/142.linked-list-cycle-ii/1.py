"""
方法一: 哈希表

解题思路：
使用哈希表来存储所有已经访问过的节点。
每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，直接返回当前节点即可；否则就将该节点加入哈希表中
重复这一过程，直到我们遍历完整个链表即可

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。最坏情况下我们需要遍历每个节点一次。
空间复杂度：O(n)。主要为哈希表的开销，最坏情况下我们需要将每个节点插入到哈希表中一次
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()

        cur = head
        while cur:
            if cur in seen:
                return cur

            seen.add(cur)
            cur = cur.next

        return None
