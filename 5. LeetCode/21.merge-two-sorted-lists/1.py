"""
方法一：迭代
https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/

解题思路：
假设有序链表 l1 的长度是 n，有序链表 l2 的长度是 m，如何在 O(n) 的时间代价以及 O(1) 的空间代价完成合并？
通过链表的第一个节点就能依次遍历完整个链表，所以题目的输入是链表 l1 和链表 l2 的第一个节点，输出是合并后新链表的第一个节点(肯定是 l1 或 l2 的第一个节点)

题目要求算法的空间复杂度是 O(1)，单链表其实就是通过节点的 next 指针来串联起各个节点的，所以我们只需要改变各节点的 next 指向就可以构建出新的链表了(新链表的节点不是新建的!)
注意: 这里我们需要为合并后新链表创建一个哨兵头节点，这样可以极大的简化 tail.next 判断逻辑，否则就需要判断新链表是否是空链表的特殊情况('NoneType' object has no attribute 'next')
1. 创建哨兵(sentinel)头节点 root，它的 val 值随意。并且使用 tail 指针表示合并后新链表的「最后一个节点」
2. 每次比较 l1 和 l2 的第一个节点，然后用 tail.next 指向较小的节点
3. 假设步骤 2 中较小的节点为 l1 的第一个节点，则向后移动 l1 指针(指向未合并部分的第一位)
4. 向后移动 tail 指针，始终表示新链表的「最后一个节点」
5. 重复步骤 2 - 4，直到 l1 或 l2 其中一个链表为空时，再把 tail.next 指向不为空的另一个链表即可
6. 返回哨兵头节点的 next 指针即可

复杂度分析：
时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。
因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中，因此 while 循环的次数不会超过两个链表的长度之和。
所有其他操作的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)。

空间复杂度：O(1)。我们只需要常数的空间存放若干变量。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(None)  # 哨兵(sentinel)头节点
        tail = root  # 表示合并后新链表的「最后一个节点」

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1  # tail 指向 l1 所在的节点
                l1 = l1.next  # l1 指针后移
            else:
                tail.next = l2  # tail 指向 l2 所在的节点
                l2 = l2.next  # l2 指针后移

            tail = tail.next  # tail 指针后移

        """
        # 下面是错误的解法，因为这样操作后，合并后的链表的所有节点都是新创建的，空间复杂度为 O(n + m)，而且实际开发中需要保持链表中的原始节点不变(id不变、内存地址不变)
        while l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)  # 创建新节点，值为 l1 节点的值
                l1 = l1.next  # l1 指针后移
            else:
                node = ListNode(l2.val)  # 创建新节点，值为 l2 节点的值
                l2 = l2.next  # l2 指针后移

            # 在 tail 节点后面插入新节点 node
            tail.next = node
            tail = node
        """

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        # if l1:  # l1 可能还有剩余节点时
        #     tail.next = l1
        # else:  # l2 可能还有剩余节点时
        #     tail.next = l2
        tail.next = l1 or l2  # 逻辑运算 x or y 表示：如果表达式 x 为真，则返回 x 的计算值，否则返回 y 的计算值

        return root.next  # 新链表的第一个节点即为哨兵头节点的 next 指向的节点
