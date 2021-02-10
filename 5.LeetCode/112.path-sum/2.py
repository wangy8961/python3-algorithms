"""
方法二: 广度优先搜索(BFS)

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 遍历树的每个节点，使用队列保存 (节点，根节点到节点的路径) 元组
2. 若当前节点是叶子节点，并且节点的路径刚好等于 sum，说明二叉树中存在根节点到叶子节点的路径等于 sum


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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, root.val)]  # 创建队列，根节点及它对应的路径组成的元组入队
        while queue:
            cur, path = queue.pop(0)
            if cur.left is None and cur.right is None and path == targetSum:  # leaf node. 注意：只有叶子节点才判断路径是否等于 sum
                return True
            if cur.left is not None:
                queue.append((cur.left, path + cur.left.val))  # 左子节点入队
            if cur.right is not None:
                queue.append((cur.right, path + cur.right.val))  # 右子节点入队

        return False  # 当队列为空时，说明不存在根节点到叶子节点的路径等于 targetSum
