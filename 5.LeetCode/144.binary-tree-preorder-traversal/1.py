"""
方法一: 深度优先搜索(DFS) - 递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/

解题思路：
什么是二叉树的前序遍历：按照访问「根节点、左子树、右子树」的方式遍历这棵树，
而在访问左子树或者右子树的时候，我们按照同样的方式遍历，直到遍历完整棵树。
因此整个遍历过程天然具有递归的性质，我们可以直接用递归函数来模拟这一过程


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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def _dfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            _dfs(root.left)
            _dfs(root.right)

        res = []
        _dfs(root)
        return res
