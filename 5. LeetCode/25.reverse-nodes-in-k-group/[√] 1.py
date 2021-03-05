"""
方法一: 
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/

解题思路：
假设链表中间长度为 k 的子链表的第一个节点为 head、最后一个节点为 tail
x -> {head -> ... -> tail} -> y
其中 y 可以由 tail.next 获取，问题在与 x 没办法获取，需要使用额外的指针 prev_node 记录
那么反转子链表 {head -> ... -> tail} 变成 {None <- head <- ... <- tail} 后，再将它加入原链表
因为反转过程中，原始头指针会不停变化，所以增加 root 哨兵头节点，一开始就指向原始链表的第一个节点，所以最后返回 root.next 即可！

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。head 指针会在 O(⌊n/k⌋) 个节点上停留，每次停留需要进行一次 O(k) 次反转指针的操作。
空间复杂度：O(1)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        root = ListNode(None)  # 哨兵(sentinel)头节点
        root.next = head

        prev_node = root
        tail = prev_node
        while True:
            for i in range(k):
                tail = tail.next
                if not tail:  # 表示第一个节点为 head、最后一个节点为 tail 的子链表长度不足 k
                    return root.next

            # 反转前，记录 tail 后续的子链，防止丢失
            next_node = tail.next

            # 反转第一个节点为 head、最后一个节点为 tail 的子链表
            new_head, new_tail = self.reverse(head, tail)

            # 将反转后的子链表接入原始链表
            prev_node.next = new_head
            new_tail.next = next_node

            # 后移 prev_node、head、tail 指针
            prev_node = new_tail
            head = next_node
            tail = prev_node

        return root.next

    def reverse(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        prev = None
        cur = head

        while prev != tail:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return tail, head
