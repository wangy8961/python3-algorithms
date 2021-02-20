"""
方法一: 广度优先搜索(BFS)
https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

解题思路：
首先我们引入一个队列：
1. 队列中一开始只存放「当前层的所有节点」
2. 先记录这一层的节点数 size (队列中元素个数)
3. 迭代 size 次，每次出队一个元素，将它的值添加到结果中，并获取它的左右子节点再入队
4. 迭代完 size 次后，队列中就是下一层的所有节点
5. 重复步骤 1 - 4 直到队列为空

重点：
通过 for 循环依次让队列元素出队前，队列中保存的是「当前层的所有节点」。
依次出队一个元素，获取它的左右子节点入队。
for 循环结束后，队列中保存的是「下一层的所有节点」。
关键是如何控制 for 循环的次数！

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
        while que:  # 如果队列不为空，说明还没有遍历完整棵树
            size = len(que)  # 每一层的节点个数
            temp = []
            for i in range(size):
                cur = que.pop(0)  # 依次将「当前层的所有节点」出队，由 size 正确计算出应该出队多少个节点
                temp.append(cur.val)
                if cur.left:
                    que.append(cur.left)  # 左子节点入队
                if cur.right:
                    que.append(cur.right)  # 右子节点入队
            res.append(temp)  # 添加到结果中

        return res
