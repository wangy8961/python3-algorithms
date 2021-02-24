"""
方法一：迭代
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

解题思路：
假设有序链表 l1 的长度是 n，有序链表 l2 的长度是 m，如何在 O(n) 的时间代价以及 O(1) 的空间代价完成合并？
为了达到空间代价是 O(1)，我们的宗旨是「原地调整链表元素的 next 指针完成合并」

复杂度分析：
时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中，因此 while 循环的次数不会超过两个链表的长度之和。所有其他操作的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)。
空间复杂度：O(1)。我们只需要常数的空间存放若干变量。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)  # 哨兵头节点(sentinel)
        cur = root  # 游标，指向合并后的链表的最新节点

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1  # cur 指向 l1 所在的节点
                l1 = l1.next  # l1 指针后移
            else:
                cur.next = l2  # cur 指向 l2 所在的节点
                l2 = l2.next  # l2 指针后移

            cur = cur.next  # cur 指针后移

        """
        # 下面是错误的解法，因为这样操作后，合并后的链表的所有节点都是新创建的，空间复杂度为 O(n + m)
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)  # 创建新节点，值为 l1 节点的值
                l1 = l1.next  # l1 指针后移
            else:
                node = ListNode(l2.val)  # 创建新节点，值为 l2 节点的值
                l2 = l2.next  # l2 指针后移

            # 在 cur 节点后面插入新节点 node
            cur.next = node
            cur = node
        """

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        # if l1:  # l1 可能还有剩余节点时
        #     cur.next = l1
        # else:  # l2 可能还有剩余节点时
        #     cur.next = l2
        cur.next = l1 or l2  # 逻辑运算 x or y 表示：如果 x 是非 0，它返回 x 的计算值，否则它返回 y 的计算值

        return root.next  # 新链表的第一个节点即为哨兵头节点的 next 指向的节点
