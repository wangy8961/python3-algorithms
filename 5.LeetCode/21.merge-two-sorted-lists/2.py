"""
方法二：递归
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/yi-kan-jiu-hui-yi-xie-jiu-fei-xiang-jie-di-gui-by-/  (看图更直观)

解题思路：
假设有序链表 l1 的长度是 n，有序链表 l2 的长度是 m
1. 判断 l1 和 l2 头结点哪个更小，然后较小结点的 next 指针指向「其余结点的合并结果(递归调用)」
2. 终止条件：当两个链表都为空时，表示我们对链表已合并完成

复杂度分析：
时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。因为每次调用递归都会去掉 l1 或者 l2 的头节点（直到至少有一个链表为空），函数 mergeTwoList 至多只会递归调用每个节点一次。因此，时间复杂度取决于合并后的链表长度，即 O(n+m)。
或者这样分析，递归函数每次去掉一个元素，直到两个链表都为空，因此需要调用 R=O(m+n) 次。而在递归函数中我们只进行了 next 指针的赋值操作，复杂度为 O(1)，故递归的总时间复杂度为 O(T)=R∗O(1)=O(m+n)

空间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。递归调用 mergeTwoLists 函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度。结束递归调用时 mergeTwoLists 函数最多调用 n+m 次，因此空间复杂度为 O(n+m)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:  # 递归退出条件
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)  # 较小结点 l1 的 next 指针指向「其余结点的合并结果」
            return l1  # 返回合并后链表的第一个节点
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)  # 较小结点 l2 的 next 指针指向「其余结点的合并结果」
            return l2  # 返回合并后链表的第一个节点
