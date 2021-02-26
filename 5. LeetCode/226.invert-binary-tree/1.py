"""
方法一: 深度优先搜索(DFS) 之 "自顶向下" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/

解题模板：
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans

适用场景：
当遇到树问题时，请先思考一下两个问题：
1. 如果你能确定一些参数，那么从该节点自身出发，你能计算出答案吗？
2. 你可以使用这些参数和节点自身的值来决定传递给它的左右子节点的参数吗？

解题思路：
如果根节点存在，交换它的左右节点
再递归交换它的左子树和右子树的左右节点即可


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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:  # 递归终止条件
            return root

        root.left, root.right = root.right, root.left  # 交换左、右节点 (实际上会把左右子树对调)
        self.invertTree(root.left)  # 递归反转左子树
        self.invertTree(root.right)  # 递归反转右子树

        return root
