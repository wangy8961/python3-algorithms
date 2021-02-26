"""
方法二: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题思路：
引入两个队列：
1. cur_que 保存「当前层的所有节点」
2. next_que 保存「下一层的所有节点」


时间复杂度：O(n)，其中 n 为二叉树节点的个数。每个节点只会被遍历一次。
空间复杂度：取决于队列中存储的最大元素个数，其在最坏情况下会达到 O(n)。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        cur_que = [root]  # 创建队列，保存「当前层的所有节点」。第一层的所有节点先进入队列
        next_que = []  # 创建队列，保存「下一层的所有节点」

        while cur_que:  # 如果队列不为空，说明还没有遍历完整棵树
            temp = []
            while cur_que:
                cur = cur_que.pop(0)  # 依次将「当前层的所有节点」出队
                temp.append(cur.val)
                if cur.left:
                    next_que.append(cur.left)  # 左子节点入队
                if cur.right:
                    next_que.append(cur.right)  # 右子节点入队
            res.append(temp)  # 添加到结果中

            cur_que, next_que = next_que, cur_que  # cur_que 重新指向 next_que，而 next_que 重新置空

        return res
