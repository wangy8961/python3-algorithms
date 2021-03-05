"""
方法二：
目标链表即为将原链表的左半段和反转后的右半段合并后的结果，所以：
1. 寻找原始链表的中间节点
2. 左半段: 以中间节点为最后一个节点的子链表；右半段: 以中间节点的后继节点为第一个节点的子链表
3. 反转右半段的子链表
4. 合并两个子链表

复杂度分析:
时间复杂度：O(n)，其中 n 是链表中的节点数。
空间复杂度：O(1)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        # 1. 寻找中间节点
        mid = self.get_middle_node(head)

        # 2. 划分左、右子链表
        right = mid.next

        mid.next = None
        left = head

        # 3. 反转右半段的子链表
        right = self.reverse(right)

        # 4. 合并
        return self.merge(left, right)

    def get_middle_node(self, head: ListNode) -> ListNode:
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)
        tail = root

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return root.next
