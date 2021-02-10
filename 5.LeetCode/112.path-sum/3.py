"""
方法三: 深度优先搜索(DFS)
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/di-gui-bfsdfsde-3chong-jie-jue-fang-shi-by-sdwwld/

解题思路：
1. 将节点和它对应的路径一起压栈
2. 节点出栈后，若当前节点就是叶子节点，并且节点的路径刚好等于 sum，说明二叉树中存在根节点到叶子节点的路径等于 sum
3. 节点的左右子节点的路径为节点路径加上左右子节点的值 path + val
4. 右子节点先入栈、左子节点后入栈。类似于「前序遍历」


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被访问一次。
空间复杂度：此方法空间的消耗取决于栈存储的元素数量，其在最坏情况下会达到 O(n)。
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

        stack = [(root, root.val)]  # 创建栈，根节点和它对应的路径组成的元组入栈
        while stack:  # 如果栈不为空，说明还没有遍历完整棵树
            cur, path = stack.pop()  # 出栈，元组解包
            if cur.left is None and cur.right is None and path == targetSum:  # leaf node. 注意：只有叶子节点才判断路径是否等于 sum
                return True
            if cur.right is not None:
                stack.append((cur.right, path + cur.right.val))  # 右子节点入栈
            if cur.left is not None:
                stack.append((cur.left, path + cur.left.val))  # 左子节点入栈

        return False  # 当栈为空时，说明不存在根节点到叶子节点的路径等于 targetSum
