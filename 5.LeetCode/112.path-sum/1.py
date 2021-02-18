"""
方法一: 深度优先搜索(DFS) 之 "自顶向下" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题模板：
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans

适用场景：
当遇到树问题时，请先思考一下两个问题：
1. 如果你能确定一些参数，那么从该节点自身出发，你能计算出答案吗？
2. 你可以使用这些参数和节点自身的值来决定传递给它的左右子节点的参数吗？(sum - val)

解题思路：
是否存在从当前节点 root 到叶子节点的路径，满足其路径和为 sum。
假定从根节点到当前节点的值之和为 val，我们可以将这个大问题转化为一个小问题：是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val。
1. 若当前节点是叶子节点，那么我们直接判断 val 是否等于 sum 即可
2. 若当前节点不是叶子节点，我们只需要递归地询问它的子节点是否能满足条件即可


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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:  # leaf node
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
