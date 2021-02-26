"""
方法一: 顺序合并

解题思路：
根据 LeetCode 21，我们已经可以合并两个有序链表了。时间复杂度：O(n)，空间复杂度：O(1)
那么可以使用 ans 保存 K 个有序链表的合并结果，第 i 次循环把第 i 个链表和 ans 合并，答案保存到 ans 中即可

复杂度分析：
时间复杂度：假设每个链表的最长的长度是 n。在第一次合并后，ans 的长度为 n；第二次合并后，ans 的长度为 2n，第 i 次合并后，ans 的长度为 i * n。
第 i 次合并的时间代价主要为遍历两个链表中的每个节点，所以是 O((i−1) * n) + O(n)= O(i * n)，
那么总的时间代价为等差数列求和 O((1+k)*k/2 * n) = O(k^2 * n)，故渐进时间复杂度为 O(k^2 * n)

空间复杂度：O(1)。我们只需要常数的空间存放若干变量。
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
        ans = None  # empty list
        for i in range(len(lists)):
            ans = self.merge_two_lists(ans, lists[i])
        return ans
