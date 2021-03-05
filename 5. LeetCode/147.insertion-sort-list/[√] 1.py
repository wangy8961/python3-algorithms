"""
方法一
https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/ (画图)

解题思路：
1. 假设原链表的第一个节点属于已排序部分，tail 表示已排序部分的「最后一个节点」
2. cur 表示未排序部分的「第一个节点」，为它在已排序部分找到正确的待插入位置即可
3. 比较 tail 和 cur 的值：
    (1) 如果 tail.val <= cur.val，说明 cur 指向的节点不用挪动，位置正确。tail 指针后移即可
    (2) 否则需要从链表的 head 开始查找第一个比 cur 值大的节点 x，用 prev 表示 cur 最终正确位置的前一个节点，即：prev -> cur -> x(prev.next)。
        在 prev 后面插入 cur 节点前，需要先让 tail 指向 cur 的后续节点(防止子链丢失)
4. 让 cur 重新指向剩余的未排序部分的「第一个节点」
5. 重复步骤 3 - 4，直到链表尾部(cur = None)
6. 返回哨兵头节点的 next 指针，即为排序后新链表的第一个节点

复杂度分析：
时间复杂度：O(n^2)，其中 n 为链表的长度。
对于链表而言，插入元素时只要更新相邻节点的指针即可，不需要像数组一样将插入位置后面的元素往后移动，因此插入操作的时间复杂度是 O(1)，
但是找到插入位置需要遍历链表中的节点，时间复杂度是 O(n)，因此链表插入排序的总时间复杂度仍然是 O(n^2)

空间复杂度：O(1)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:  # 空链表
            return head

        root = ListNode(None)  # 哨兵(sentinel)头节点，方便在 head 前面插入节点
        root.next = head  # 头节点指向原链表的第一个节点

        tail = head  # 表示已排序部分的「最后一个节点」，一开始只有原链表的第一个节点属于已排序的
        cur = head.next  # 表示未排序部分的「第一个节点」，为它在已排序部分找到正确的待插入位置即可
        while cur:
            if tail.val <= cur.val:  # cur 指向的节点不用挪动，位置正确。tail 指针后移即可
                tail = cur  # 或 tail = tail.next，因为它俩是挨着的
            else:  # 从链表的 head 开始查找第一个比 cur 值大的节点 x，用 prev 表示 cur 最终正确位置的前一个节点，即：prev -> cur -> x(prev.next)
                prev = root
                while prev.next.val <= cur.val:
                    prev = prev.next
                # 此时 prev.next 就是第一个比 cur 值大的节点 x

                tail.next = cur.next  # 防止 cur 后面的子链被丢失

                # 在 prev 节点后面插入 cur，标准的链表插入操作
                cur.next = prev.next
                prev.next = cur

            cur = tail.next  # cur 重新指向剩余的未排序部分的「第一个节点」，直到链表尾部(cur = None)

        return root.next  # 返回哨兵头节点的 next 指针
