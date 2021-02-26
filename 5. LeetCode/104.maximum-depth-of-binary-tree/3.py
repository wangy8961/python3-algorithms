"""
方法三: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题思路：
首先我们引入一个队列，这是把递归程序改写成迭代程序的常用方法。
1. 队列中只存放「某一层的所有节点」
2. 先记录这一层的节点数 size (队列中元素个数)
3. 迭代 size 次，每次出队一个元素，获取它的左右子节点再入队
4. 迭代完 size 次后，队列中就是下一层的所有节点。将最终结果 ans 值加 1
5. 重复步骤 1 - 4。二叉树的最大深度即为 ans


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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = [root]  # 创建队列，第一层的所有节点先进入队列
        ans = 0

        while que:  # 如果队列不为空，说明还没有遍历完整棵树
            size = len(que)  # 每一层的节点个数
            for i in range(size):
                cur = que.pop(0)  # 依次将「当前层的所有节点」出队，由 size 正确计算出应该出队多少个节点
                if cur.left:
                    que.append(cur.left)  # 左子节点入队
                if cur.right:
                    que.append(cur.right)  # 右子节点入队

            ans += 1  # 层数加 1，因为 ans 初始值为 0

        return ans
