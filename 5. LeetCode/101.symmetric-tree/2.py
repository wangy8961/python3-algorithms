"""
方法二: 迭代

解题思路：
如果一个树的左子树与右子树是镜像对称的，那么这颗树就是对称的。因此，该问题可以转化为：两颗树在什么情况下互为镜像？
两颗树同时满足下面的条件时互为镜像：
1. 它们的两个根节点具有相同的值
2. 每颗树的右子树都与另一颗树的左子树镜像对称

首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 初始化时我们把两颗子树的根节点入队。
2. 每次出队两个节点并比较它们的值（队列中每两个连续的节点应该是相等的，而且它们的子树互为镜像），然后将两个节点的左右子节点按相反的顺序插入队列中。
3. 当队列为空时，或者我们检测到树不对称时（即从队列中取出的两个连续节点不相等），该算法结束。


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被访问一次。
空间复杂度：取决于队列中存储的最大元素个数，其在最坏情况下会达到 O(n)。
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
        # 两颗子树的根节点入队
        que.append(root)
        que.append(root)

        while que:
            p, q = que.pop(0), que.pop(0)  # 每次出队两个节点
            if not p and not q:
                continue
            if not p or not q:
                return False  # 检测到树不对称
            if p.val != q.val:
                return False  # 检测到树不对称

            # 将两个节点的左右子节点按相反的顺序插入队列中
            que.append(p.left)
            que.append(q.right)

            que.append(p.right)
            que.append(q.left)

        return True  # 当队列为空时，也没有检测到树不对称，说明是对称二叉树
