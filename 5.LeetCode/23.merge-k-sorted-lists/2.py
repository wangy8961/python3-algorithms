"""
方法二: 分治合并

解题思路：
根据 LeetCode 21，我们已经可以合并两个有序链表了。时间复杂度：O(n)，空间复杂度：O(1)

合并函数 merge_two_lists 输入是两个有序链表的第一个节点，输出是新链表的第一个节点
将 k 个有序链表的第一个节点组成的序列 lists，通过分治思想，两两合并形成一个新链表

复杂度分析：
时间复杂度：假设每个链表的最长的长度是 n。
第一轮合并时，两个链表分一组，共 k/2 个组，每一组的时间代价就是遍历合并 2n 个链表节点，即 O(2n)。共需 O(kn) 时间复杂度
第二轮合并时，两个链表分一组，共 k/4 个组，每一组的时间代价就是遍历合并 4n 个链表节点，即 O(4n)。共需 O(kn) 时间复杂度
...
共需 logk 轮合并，所以总的渐进时间复杂度为 O(kn * logk)

空间复杂度：递归会使用到 O(logk) 的栈空间。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)
        tail = root

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return root.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """lists 中存放的是 K 个有序链表的第一个节点"""
        n = len(lists)

        # 递归退出条件
        if n == 0:  # 没有链表时
            return None  # 空链表
        if n == 1:  # 仅一个链表，肯定是有序的。类比归并排序中数组的一个元素
            return lists[0]

        mid = n // 2
        left = self.mergeKLists(lists[:mid])  # 递归计算左边，left 表示新链表的第一个节点
        right = self.mergeKLists(lists[mid:])  # 递归计算右边，right 表示新链表的第一个节点

        return self.merge_two_lists(left, right)  # 合并左右两个有序链表
