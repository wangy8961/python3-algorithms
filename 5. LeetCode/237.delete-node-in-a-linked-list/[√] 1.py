"""
方法一: 与后继节点交换值

解题思路：
题目输入只有当前链表节点，单链表没有头指针的情况下，我们没办法从当前节点获取它的前驱节点
因为题目明确说明了链表中所有节点的值都是唯一的，所以可以将当前节点和后继节点交换值，问题转换为删除后继节点即可
因为题目明确说明了当前节点不是链表末尾，所以当前节点肯定有后继节点！


复杂度分析：
时间复杂度：O(1)。
空间复杂度：O(1)。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next  # 当前节点 node 的后继节点
        node.val = next_node.val  # 与后继节点交换值
        node.next = next_node.next  # 然后删除当前节点 node 的后继节点

        # 简写为
        # node.val = node.next.val
        # node.next = node.next.next
