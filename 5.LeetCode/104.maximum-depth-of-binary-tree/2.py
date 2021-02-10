"""
方法二: 深度优先搜索(DFS) 之 "自顶向下" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题模板：
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)		// left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)	// right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans

何时使用：
当遇到树问题时，请先思考一下两个问题：
1. 你能确定一些参数，从该节点自身出发寻找答案吗？(根节点的深度是 1。对于每个节点，如果我们知道某节点的深度，那我们将知道它子节点的深度。因此，在调用递归函数的时候，将节点的深度传递为一个参数，那么所有的节点都知道它们自身的深度。而对于叶节点，我们可以通过更新深度从而获取最终答案)
2. 你可以使用这些参数和节点自身的值来决定传递给它的左右子节点的参数吗？(depth + 1)

时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点在递归中只被遍历一次。
空间复杂度：O(height)，其中 height 表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，因此空间复杂度等价于二叉树的高度。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0  # don't forget to initialize answer before call _top_down

        def _top_down(root: TreeNode, depth: int) -> int:
            if not root:
                return
            if root.left is None and root.right is None:  # leaf node
                nonlocal ans
                ans = max(ans, depth)
            _top_down(root.left, depth + 1)
            _top_down(root.right, depth + 1)

        _top_down(root, 1)  # the depth of root node is 1
        return ans
