"""
方法三: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 队列里存放的是「当前层的所有节点」
2. 每次拓展下一层的时候，不同于「普通的广度优先搜索」的每次只从队列里拿出一个节点，我们需要将队列里的所有节点都拿出来进行拓展，这样能保证每次拓展完的时候队列里存放的是当前层的所有节点，即我们是一层一层地进行拓展，最后我们用一个变量 ans 来维护拓展的次数，该二叉树的最大深度即为 ans


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被访问一次。
空间复杂度：此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)。
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
        queue = [root]  # 创建队列，第一层的所有节点先进入队列
        ans = 0

        while queue:  # 如果队列不为空，说明还没有遍历完整棵树
            size = len(queue)  # 每一层的节点个数
            for i in range(size):
                cur = queue.pop(0)  # 依次将「当前层的所有节点」出队，由 size 正确计算应该出队多少个节点
                if cur.left is not None:
                    queue.append(cur.left)  # 左子节点入队
                if cur.right is not None:
                    queue.append(cur.right)  # 右子节点入队

            ans += 1  # 层数加 1，因为 ans 初始值为 0

        return ans
