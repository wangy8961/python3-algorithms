"""
方法二: 广度优先搜索(BFS)

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 遍历树的每个节点，使用队列保存 (节点，根节点到节点的路径) 元组
2. 若当前节点是叶子节点，并且节点的路径刚好等于 sum，说明二叉树中存在根节点到叶子节点的路径等于 sum


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被遍历一次。
空间复杂度：取决于队列中存储的最大元素个数，其在最坏情况下会达到 O(n)。
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
        que = [(root, root.val)]  # 创建队列，根节点及它对应的路径组成的元组入队
        while que:
            cur, path = que.pop(0)
            if not cur.left and not cur.right and path == targetSum:  # leaf node. 注意：只有叶子节点才判断路径是否等于 sum
                return True
            if cur.left:
                que.append((cur.left, path + cur.left.val))  # 左子节点入队
            if cur.right:
                que.append((cur.right, path + cur.right.val))  # 右子节点入队

        return False  # 当队列为空时，说明不存在根节点到叶子节点的路径等于 targetSum
