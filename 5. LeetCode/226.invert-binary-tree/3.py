"""
方法三: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 根节点先入队
2. 交换其左右节点
3. 如果左节点不为空，入队；如果右节点不为空，入队
4. 重复步骤 2 - 3，直到队列为空


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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        que = [root]  # 创建队列，根节点先进入队列
        while que:  # 如果队列不为空，说明还没有遍历完整棵树
            cur = que.pop(0)  # 依次出队
            cur.left, cur.right = cur.right, cur.left  # 交换左、右节点
            if cur.left:
                que.append(cur.left)  # 左子节点入队
            if cur.right:
                que.append(cur.right)  # 右子节点入队

        return root
