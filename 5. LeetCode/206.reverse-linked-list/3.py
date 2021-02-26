"""
方法三: 双头指针(head 和 cur)
https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/

解题思路：
1. head 始终指向原始链表的「第一个节点」
2. 用 cur 表示已逆序的新链表的「第一个节点」，初始化为 head
3. 用 head.next 表示未逆序的子链的「第一个节点」
4. 每次都让 head.next 所在节点的 next 指针指向 cur，实现一次局部逆序
5. 然后让 cur 和 head.next 指针同时右移
6. 重复步骤 4 - 5，直到 head.next 为 None(即 head 指向 None，全部节点逆序完成)
7. 返回新链表的头指针 cur 即可

看图更直观，假设原始链表为 1 → 2 → 3 → 4 → 5 → ∅，初始状态为：

  ↑￣￣↓
  1    2 → 3 → 4 → 5 → ∅
head
 cur

其中一次局部逆序前的状态为：

  ↑￣￣￣￣￣￣↓
  1 ← 2 ← 3   4 → 5 → ∅
head     cur

本次逆序操作完成后的状态为：

  ↑￣￣￣￣￣￣￣￣↓
  1 ← 2 ← 3 ← 4   5 → ∅
head         cur

整个链表最终全部逆序完成时：

  ↑￣￣￣￣￣￣￣￣￣￣↓
  1 ← 2 ← 3 ← 4 ← 5  ∅
head             cur


复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
空间复杂度：O(n)。由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:  # 空链表
            return head

        cur = head  # cur 表示已逆序的新链表的「第一个节点」
        while head.next:  # head.next 表示未逆序的子链的「第一个节点」
            temp = head.next.next  # 保存 head.next 节点的后继节点，防止子链丢失
            head.next.next = cur  # 让 head.next 所在节点的 next 指针指向 cur，实现一次局部逆序
            cur = head.next  # 让 cur 指针右移
            head.next = temp  # 让 head.next 指针右移，即原始链表的「第一个节点」改为指向 temp

        # 上面的 while 循环内部可以简写为一行，原地交换
        # while head.next:
        #     head.next.next, cur, head.next = cur, head.next, head.next.next

        return cur
