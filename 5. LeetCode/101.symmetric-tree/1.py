"""
方法一: 深度优先搜索(DFS)

解题思路：
如果一个树的左子树与右子树是镜像对称的，那么这颗树就是对称的。因此，该问题可以转化为：两颗树在什么情况下互为镜像？
两颗树同时满足下面的条件时互为镜像：
1. 它们的两个根节点具有相同的值
2. 每颗树的右子树都与另一颗树的左子树镜像对称

我们可以实现一个递归函数，通过「同步移动」两个指针的方法来遍历这棵树，p 指针和 q 指针一开始都指向两棵树的根节点，
随后 p 右移时，q 左移；p 左移时，q 右移。每次检查当前 p 和 q 节点的值是否相等，如果相等再继续判断左右子树是否对称。


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(h)，其中 h 是树的高度。空间复杂度主要取决于递归时栈空间的开销，最坏情况下，树呈现链状，空间复杂度为 O(n)。平均情况下树的高度与节点数的对数正相关，空间复杂度为 O(logn)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)

    def check(self, p: TreeNode, q: TreeNode) -> bool:
        # 递归退出条件
        if not p and not q:  # 两棵空树
            return True
        if not p or not q:  # 只有一课空树
            return False

        # 根节点的值相等，且p的左子树与q的右子树互为镜像、p的右子树与q的左子树互为镜像
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
