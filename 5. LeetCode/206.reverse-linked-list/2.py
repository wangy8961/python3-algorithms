"""
方法二: 递归

解题思路：
假设原始链表有 n 个节点，除了第一个节点外其余节点全部逆序完毕(把它们想象成一个整体 x 即可)
递归函数返回指针 p，表示逆序后新链表的「头指针」

那么现在就剩下原始链表的第一个节点(head)和新链表的最后一个节点(head.next)之间的逆序操作了：
head.next.next = head
head.next = None

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
空间复杂度：O(n)。由于使用递归，将会使用隐式栈空间。每次递归逆序一个节点，除第一个节点外需要递归 n - 1 次，所以渐进空间复杂度为 O(n)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归的终止条件
        if not head:  # 空链表
            return head
        if not head.next:  # 1. 原始链表只有一个节点时 2. 已经是原始链表的最后一个节点时
            return head  # 新链表的头指针必定指向原始链表的最后一个节点

        p = self.reverseList(head.next)  # 假设将当前节点之后的链表逆序完成，并返回逆序后新链表的「头指针」
        # 原始链表第一个节点(head)和新链表的最后一个节点(head.next)之间的逆序操作
        head.next.next = head
        head.next = None

        return p  # 返回新链表的头指针
