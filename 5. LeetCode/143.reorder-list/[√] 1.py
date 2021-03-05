"""
方法一：数组
因为链表不支持下标访问，所以我们无法随机访问链表中任意位置的元素
可以利用数组存储该链表，然后利用数组按下标随机访问的特点，直接按顺序访问指定元素，重建该链表即可

复杂度分析:
时间复杂度：O(n)，其中 n 是链表中的节点数。
空间复杂度：O(n)，主要为线性表的开销。
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

        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next

        i, j = 0, len(arr) - 1
        while i < j:
            arr[i].next = arr[j]
            i += 1
            if i == j:
                break

            arr[j].next = arr[i]
            j -= 1

        arr[i].next = None
