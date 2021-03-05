"""
方法二: 快慢指针 + 数学公式

解题思路：
https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/xiang-xi-tu-jie-ken-ding-kan-de-ming-bai-by-xixili/

相遇时：
slow走过的路程：x + y + n(y+z), n代表slow绕了n圈
fast走过的路程：x + y + m(y+z)，m代表fast饶了m圈，m > n

因为fast速度是slow两倍：
2(x + y + n(y + z)) = x + y + m(y + z)

x + y = (m - 2n)(y + z)
x = (m - 2n)(y + z) - y
y + z就是1圈，假设 o = m-2n，o是一个正整数，那么 x = o(y + z) -y

如果o = 1，那么 x = z，和答主假设的情况一样
如果o > 1，那么 x = (o-1)(y+z) + y + z - y, x = (o-1)(y+z) + z，即x的长度为o-1圈加上z

所以，从第一阶段获得的相遇点，走过x距离机会到达环的起点。


复杂度分析：
时间复杂度：O(n)，其中 n 是链表的节点数量。
在最初判断快慢指针是否相遇时，slow 指针走过的距离不会超过链表的总长度；随后寻找入环点时，走过的距离也不会超过链表的总长度。
因此，总的执行时间为 O(n) + O(n) = O(n)。

空间复杂度：O(1)。我们只使用了 slow, fast, p 三个指针的额外空间
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:  # 快指针遍历完整个链表了，也没有与慢指针相遇，表示链表无环
                return None

            slow = slow.next
            fast = fast.next.next

            if fast == slow:  # 快、慢指针在环内相遇了
                break

        # p 走到环入口时，slow 指针肯定也刚好又走到了环入口
        p = head
        while p != slow:
            p = p.next
            slow = slow.next

        return p
