"""
方法一: 深度优先搜索(DFS)

解题思路：
如果一个树的左子树与右子树镜像对称，那么这个树是对称的。
因此，该问题可以转化为：两个树在什么情况下互为镜像？如果同时满足下面的条件，两个树互为镜像：
1. 它们的两个根节点具有相同的值
2. 每个树的右子树都与另一个树的左子树镜像对称

我们可以实现这样一个递归函数，通过「同步移动」两个指针的方法来遍历这棵树，p 指针和 q 指针一开始都指向这棵树的根，
随后 p 右移时，q 左移；p 左移时，q 右移。每次检查当前 p 和 q 节点的值是否相等，如果相等再判断左右子树是否对称。


时间复杂度：渐进时间复杂度为 O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：和递归使用的栈空间有关，这里递归层数不超过 n，渐进空间复杂度为 O(n)。
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
        if not p and not q:  # 两棵空树
            return True
        if not p or not q:  # 只有一课空树
            return False
        # 根节点相等，且p的左子树与q的右子树互为镜像、p的右子树与q的左子树互为镜像
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
