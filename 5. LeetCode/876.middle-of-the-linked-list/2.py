"""
方法二: 两次遍历

解题思路：
第一次链表遍历，求出总节点数目 n，通过公式 pos = n // 2 + 1 算出中间节点就是「第 pos 个节点 」
第二次链表遍历，返回第 pos 个节点即可

复杂度分析：
时间复杂度：O(n + n/2)，其中 n 是链表的节点数量。
空间复杂度：O(1)。只需要常数空间存放变量和指针
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n = 0  # 链表总节点数
        cur = head
        while cur:
            n += 1
            cur = cur.next

        pos = n // 2 + 1  # 计算出中间节点就是「第 pos 个节点 」

        cur = head
        for i in range(pos - 1):
            cur = cur.next

        return cur
