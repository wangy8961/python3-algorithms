"""
方法三: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题思路：
使用两个指针来记录每层的最右节点：
last 表示「当前层的最右节点」，nlast 表示「下一层的最右节点」
nlast 一直跟踪记录 '最新' 加入队列的节点即可，因为 '最新' 加入队列的节点一定是目前发现的下一层的最右孩子


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

        que = [root]  # 创建队列，第一层的所有节点先进入队列
        last = root  # 开始时，让 last 指向根节点，因为第一层只有一个节点
        nlast = None  # 开始时，让 nlast 指向空。比如，整棵树只有根节点时

        temp = []  # 将每一层的所有节点值保存为列表，用于后续添加到结果中
        while que:  # 如果队列不为空，说明还没有遍历完整棵树
            cur = que.pop(0)  # 依次出队
            temp.append(cur.val)

            if cur.left:
                que.append(cur.left)  # 左子节点入队
                nlast = cur.left
            if cur.right:
                que.append(cur.right)  # 右子节点入队
                nlast = cur.right

            if cur == last:  # 说明「当前层的所有节点」都已出队
                last = nlast
                res.append(temp)  # 添加到结果中
                temp = []  # 重新置空

        return res
