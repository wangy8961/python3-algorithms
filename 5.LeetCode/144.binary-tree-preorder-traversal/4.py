"""
方法四: Morris 遍历
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/er-cha-shu-de-qian-xu-bian-li-by-leetcode-solution/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/leetcodesuan-fa-xiu-lian-dong-hua-yan-shi-xbian-2/

解题思路：
利用二叉树中大量指向 None 的指针，可以将空间复杂度降为 O(1)
对于给定的二叉树(包括它的左右子树)，从根结点开始，找到它的左子树中「最右侧节点 p2」与这个根结点进行连接 (p2.right = p1)。
如果这么连接之后，p1 指针就可以完整的顺着一个节点到下一个节点，将整棵树遍历完毕，直到整棵树的最右侧节点 (p2.right = None)


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被遍历一次。
空间复杂度：O(1)。
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

        p1 = root
        while p1:
            p2 = p1.left
            if p2:
                while p2.right and p2.right != p1:  # 1. 找到它的左子树中「最右侧节点」
                    p2 = p2.right

                if not p2.right:
                    res.append(p1.val)
                    p2.right = p1  # 2. 与根结点进行连接
                    p1 = p1.left
                    continue
                else:
                    p2.right = None  # 3. 断开与根结点的连接，恢复二叉树
            else:  # p1 没有左子节点时
                res.append(p1.val)

            p1 = p1.right  # p1 顺序往右移动，直到整棵树的最右侧节点

        return res
