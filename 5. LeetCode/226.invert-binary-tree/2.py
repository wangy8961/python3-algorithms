"""
方法二: 深度优先搜索(DFS) 之 "自底向上" 的递归
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
https://leetcode-cn.com/problems/invert-binary-tree/solution/fan-zhuan-er-cha-shu-by-leetcode-solution/

解题模板：
1. return specific value for null node
2. left_ans = bottom_up(root.left)          // call function recursively for left child
3. right_ans = bottom_up(root.right)        // call function recursively for right child
4. return answers                           // answer <-- left_ans, right_ans, root.val

适用场景：
当遇到树问题时，请先思考一下：
对于树中的任意一个节点，如果你知道它的子节点的答案，你能计算出该节点的答案吗？

解题思路：
我们从根节点开始，递归地对树进行遍历，并从叶子结点先开始翻转。
如果当前遍历到的节点 root 的左右两棵子树都已经翻转，那么我们只需要交换两棵子树的位置，即可完成以 root 为根节点的整棵子树的翻转


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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:  # 递归终止条件
            return root

        left = self.invertTree(root.left)  # 递归反转左子树
        right = self.invertTree(root.right)  # 递归反转右子树
        root.left, root.right = right, left  # 交换左、右子树

        return root
