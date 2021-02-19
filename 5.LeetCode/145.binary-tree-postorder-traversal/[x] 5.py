"""
方法五: Morris 遍历
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/er-cha-shu-de-hou-xu-bian-li-by-leetcode-solution/
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/leetcodesuan-fa-xiu-lian-dong-hua-yan-shi-xbian-2/

解题思路：
利用二叉树中大量指向 None 的指针，可以将空间复杂度降为 O(1)


时间复杂度：O(n)，其中 n 为二叉树节点的个数。没有左子树的节点只被访问一次，有左子树的节点被访问两次。
空间复杂度：O(1)。只操作已经存在的指针（树的空闲指针），因此只需要常数的额外空间。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pass
