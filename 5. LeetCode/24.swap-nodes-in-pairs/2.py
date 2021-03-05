"""
方法二: 递归
https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/

解题思路：
假设原始链表有 n 个节点，除了前两个节点外其余节点全部两两交换完毕(把它们想象成一个整体 x 即可)
head 头指针：表示原始链表的第一个节点
new_head 头指针: 表示新链表的第一个节点
问题转化为把 head -> new_head -> x 变成 new_head -> head -> x 即可：
1. head.next = x  # 此时 head 和 new_head 都指向 x
2. new_head.next = head  # new_head 改为指向 head

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
空间复杂度：O(n)。空间复杂度主要取决于递归调用的栈空间，每次交换 2 个节点，需要 n/2 次递归操作
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 递归的终止条件是链表中没有节点，或者链表中只有一个节点，此时无法进行交换
            return head

        # 注意：步骤 2 和 3 不能调换，否则就是 new_head 和 head 互相指向，后续节点会丢失！
        new_head = head.next  # 1. 原始链表的第二个节点变成新链表的第一个节点
        head.next = self.swapPairs(new_head.next)  # 2. 递归处理其余节点
        new_head.next = head  # 3. 原始链表的第一个节点变成新链表的第二个节点

        return new_head  # 返回新链表的头指针
