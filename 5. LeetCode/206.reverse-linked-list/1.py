"""
方法一: 迭代

解题思路：
假设存在链表 1→2→3→∅，我们想要把它改成 ∅←1←2←3。在遍历链表时，将 **当前节点 cur 的 next 指针** 改为指向前驱节点即可

由于单链表中的当前节点没有引用其前驱节点，因此必须事先使用 prev 存储其前驱节点
在更改引用之前，还需要另一个指针 temp 来保存当前节点的后继节点，否则就找不到原链表中的后续节点了
不要忘记在最后返回新链表的头指针

1. 使用 prev 指针表示逆序后新链表的「第一个节点」，初始时它指向 None
2. cur 表示原始链表中未完成逆序操作的「第一个节点」，初始时它指向原始链表的第一个节点(即头指针 head 所指向的节点)
3. 问题转化为将 cur 节点插入新链表的首部(头插法)，然后向后移动 cur 指针
4. 重复步骤 3，直到全部节点逆序完成(此时 cur 指向原始链表的末尾 None)
5. 返回新链表的头指针 prev 即可

复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。需要对每个节点进行更新指针的操作。
空间复杂度：O(1)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head

        while cur:
            temp = cur.next  # 保存当前节点的后继节点，防止子链丢失
            cur.next = prev  # 逆序操作，将当前节点的 next 指针改为指向它的前驱节点
            prev = cur  # 先移动 prev 指针
            cur = temp  # 然后再移动 cur 指针

        # 上面的 while 循环内部可以简写为一行，原地交换
        # while cur:
        #     cur.next, prev, cur = prev, cur, cur.next

        return prev  # 返回新链表的头指针
