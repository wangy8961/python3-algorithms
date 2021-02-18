"""
方法二: 迭代
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/

解题思路：
使用栈来进行迭代，由于栈是 "后进先出" 的顺序，所以入栈时先将右子树入栈，这样使得前序遍历结果为「根、左、右」的顺序。过程如下：
1. 初始化栈，并将根节点入栈
2. 当栈不为空时：
  (1) 弹出栈顶元素 cur，并将它的值添加到结果中
  (2) 如果 cur 的右子节点非空，将右子节点入栈
  (3) 如果 cur 的左子节点非空，将左子节点入栈


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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = [root]  # 创建栈，根节点入栈
        while stack:
            cur = stack.pop()  # 弹出栈顶元素
            if cur:
                res.append(cur.val)  # 将栈顶元素的值添加到结果中
                if cur.right:
                    stack.append(cur.right)  # 右子节点入栈
                if cur.left:
                    stack.append(cur.left)  # 左子节点入栈

        return res
