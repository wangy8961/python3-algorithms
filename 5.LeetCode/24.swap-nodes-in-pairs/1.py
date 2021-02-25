"""
方法一: 迭代
https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/liang-liang-jiao-huan-lian-biao-zhong-de-jie-di-91/ (画图)

解题思路：
1. 创建哨兵(sentinel)头节点，并让头节点指向原链表的第一个节点
2. cur 表示当前到达的节点，每次需要交换 cur 后面的两个节点
3. 如果 cur 的后面没有节点或者只有一个节点，则没有更多的节点需要交换，因此结束交换。
否则，获得 cur 后面的两个节点 node1 和 node2，通过更新节点的指针关系实现两两交换节点
由 cur -> node1 -> node2 -> x 变成 cur -> node2 -> node1 -> x
交换之后再让 cur = node1 后移两个节点
4. 重复步骤 3，对链表中的其余节点进行两两交换，直到全部节点都被两两交换
5. 返回哨兵头节点的 next 指针，即为交换后新链表的第一个节点

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
    def swapPairs(self, head: ListNode) -> ListNode:
        root = ListNode(None)  # 哨兵(sentinel)头节点
        root.next = head  # 头节点指向原链表的第一个节点

        cur = root  # cur 表示当前到达的节点，每次需要交换 cur 后面的两个节点
        while cur.next and cur.next.next:
            node1 = cur.next  # 因为哨兵的存在，所以 node1 肯定存在
            node2 = cur.next.next

            # cur -> node1 -> node2 -> x 变成 cur -> node2 -> node1 -> x
            cur.next = node2  # 此时 cur 和 node1 都指向 node2
            node1.next = node2.next  # node1 改为指向 x，防止 x 子链表丢失
            node2.next = node1

            cur = node1  # 后移2个节点

        return root.next
