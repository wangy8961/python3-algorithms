"""
方法四: 迭代
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/

解题思路：
使用栈来进行迭代，由于栈是 "后进先出" 的顺序，如果依次将根节点、右节点、左节点压栈，再每次弹出栈顶元素，被弹出的节点相当于二叉树(或左右子树)的根节点，
为了得到后序遍历的结果「左、右、根」，需要最后输出根节点，因此需要将被弹出的节点再次压栈(此时不能打印节点值)，并依次把它的右节点、左节点压栈

注意：如果你实现了 stack，支持 peek() 操作，可以不用入栈两次，只用调用 peek() 函数获取栈顶元素值而不弹出，再将它的右节点、左节点依次压栈即可

时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点被遍历两次。
空间复杂度：取决于栈中存储的最大元素个数，其在最坏情况下会达到 O(n)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        stack = [(root, 0)]  # 创建栈，根节点和对应标志组成的元组入栈
        while stack:
            cur, flag = stack.pop()  # 弹出栈顶元素，元组解包。cur 相当于二叉树(或左右子树)的根节点，
            if flag == 0:
                stack.append((cur, 1))  # 重新将 cur 压栈，标志位修改为 1，表示入栈两次了
                if cur.right:
                    stack.append((cur.right, 0))  # 右子节点入栈
                if cur.left:
                    stack.append((cur.left, 0))  # 左子节点入栈
            else:  # 将入栈两次的 cur 的值添加到结果中
                res.append(cur.val)

        return res
