"""
方法四：回溯

找出从根节点到叶子节点的「所有完整路径」，只要有任意一条路径的和等于 sum，就表示找到了
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def _dfs(root: TreeNode, full_path: list[int]) -> bool:
            if not root:  # 叶子节点的左右子节点都是 None，递归退出条件
                return False
            if not root.left and not root.right and sum(full_path) == targetSum:  # leaf node. 注意：只有叶子节点才判断 full_path 求和后是否等于 targetSum
                # print(f'Found: {full_path}')
                return True

            left_ans, right_ans = False, False
            if root.left:
                left_ans = _dfs(root.left, full_path + [root.left.val])  # 需要创建新的列表，否则所有递归函数中都是修改同一个 full_path 列表。不能使用 full_path.append(root.left.val)
            if root.right:
                right_ans = _dfs(root.right, full_path + [root.right.val])  # 需要创建新的列表，否则所有递归函数中都是修改同一个 full_path 列表。不能使用 full_path.append(root.right.val)
            return left_ans or right_ans

        full_path = [root.val]  # 保存根节点到叶节点的完整访问路径，比如 [5, 4, 11, 2]
        return _dfs(root, full_path)
