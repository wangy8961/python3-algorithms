"""
方法四: 深度优先搜索(DFS)
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/di-gui-bfsdfsde-3chong-jie-jue-fang-shi-by-sdwwld/

解题思路：
1. 将节点和它对应的深度一起压栈
2. 节点出栈后，更新树的最大深度为 ans 和节点深度中的最大值
3. 节点的左右子节点的深度为节点深度加 1
4. 右子节点先入栈、左子节点后入栈。类似于「前序遍历」


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被遍历一次。
空间复杂度：取决于栈中存储的最大元素个数，其在最坏情况下会达到 O(n)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]  # 创建栈，根节点和它对应的深度组成的元组入栈
        ans = 0

        while stack:  # 如果栈不为空，说明还没有遍历完整棵树
            cur, depth = stack.pop()  # 出栈，元组解包
            ans = max(ans, depth)  # 有可能需要更新 ans
            if cur.right:
                stack.append((cur.right, depth + 1))  # 右子节点入栈
            if cur.left:
                stack.append((cur.left, depth + 1))  # 左子节点入栈

        return ans
