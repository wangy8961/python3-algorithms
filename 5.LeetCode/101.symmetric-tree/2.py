"""
方法二: 迭代

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 初始化时我们把根节点入队两次。
2. 每次出队两个节点并比较它们的值（队列中每两个连续的节点应该是相等的，而且它们的子树互为镜像），然后将两个节点的左右子节点按相反的顺序插入队列中。
3. 当队列为空时，或者我们检测到树不对称时（即从队列中取出的两个连续节点不相等），该算法结束。


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被访问一次。
空间复杂度：这里需要用一个队列来维护节点，每个节点最多进队一次，出队一次，队列中最多不会超过 n 个点，故渐进空间复杂度为 O(n)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        que = []  # 创建队列
        u, v = root, root
        # 根节点入队
        que.append(u)
        que.append(v)

        while que:
            u, v = que.pop(0), que.pop(0)  # 每次出队两个节点
            if not u and not v:
                continue
            if not u or not v:
                return False  # 检测到树不对称
            if u.val != v.val:
                return False  # 检测到树不对称

            # 将两个节点的左右子节点按相反的顺序插入队列中
            que.append(u.left)
            que.append(v.right)

            que.append(u.right)
            que.append(v.left)

        return True  # 当队列为空时，也没有检测到树不对称，说明是对称二叉树
