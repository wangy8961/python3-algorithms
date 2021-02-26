"""
方法三: 分治合并(优化版)

解题思路：
根据 LeetCode 21，我们已经可以合并两个有序链表了。时间复杂度：O(n)，空间复杂度：O(1)

方法二中 self.mergeKLists(lists[:mid]) 和 self.mergeKLists(lists[mid:]) 使用了列表的切片操作来获取左、右子序列，会产生新对象。
如果 lists 序列很大(即k很大)时，空间有浪费。
merge_k_lists_recurve 函数只操作同一个 lists 的下标

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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """lists 中存放的是 K 个有序链表的第一个节点"""
        return self.merge_k_lists_recurve(lists, 0, len(lists) - 1)

    def merge_k_lists_recurve(self, lists: List[ListNode], low: int, high: int) -> ListNode:
        """用于递归调用的函数，返回合并后的新链表的第一个节点"""
        # 递归退出条件
        if low > high:  # 没有链表时
            return None  # 空链表
        if low == high:  # 仅一个链表，肯定是有序的。类比归并排序中数组的一个元素
            return lists[low]

        mid = (low + high) // 2
        left = self.merge_k_lists_recurve(lists, low, mid)  # 递归计算左边
        right = self.merge_k_lists_recurve(lists, mid + 1, high)  # 递归计算右边

        return self.merge_two_lists(left, right)  # 合并左右两个有序链表

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
