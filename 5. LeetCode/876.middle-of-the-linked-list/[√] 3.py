"""
方法三: 快慢指针

解题思路：
用两个指针 slow 与 fast 一起遍历链表。slow 一次走一步，fast 一次走两步。
那么当 fast 到达链表的末尾时，slow 必然位于中间

(1) 如果有两个中间节点，则返回第二个中间节点「本题的要求」
此时，快指针可以前进的条件是：当前快指针和当前快指针的下一个节点都非空
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
(2) 如果有两个中间节点，则返回第一个中间节点
此时，快指针可以前进的条件是：当前快指针的下一个节点和当前快指针的下下一个节点都非空
while fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量
空间复杂度：O(1)。只需要常数空间存放 slow 和 fast 两个指针
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
