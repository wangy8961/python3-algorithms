"""
方法三：

解题思路：
只用一个栈，因为底层使用数组来实现栈，所以每次压栈时，将 (x, 栈内最小值的下标) 一起压栈

复杂度分析：
时间复杂度：所有操作，时间复杂度均为 O(1)。因为栈的插入、删除与读取操作都是 O(1)，我们定义的每个操作最多调用栈操作两次。
空间复杂度：O(n)，其中 n 为总操作数。最坏情况下，我们会连续插入 n 个元素，此时两个栈占用的空间为 O(n)。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:  # 栈为空
            self.stack.append((x, 0))
        else:
            _, cur_min_index = self.stack[-1]  # 元组解包
            cur_min, _ = self.stack[cur_min_index]
            # 或者:
            # cur_min = self.getMin()

            if x < cur_min:
                self.stack.append((x, len(self.stack)))  # 当前 x 插入后的下标为 len(self.stack)
            else:
                self.stack.append((x, cur_min_index))

    def pop(self) -> None:
        if not self.stack:  # 栈为空
            return

        self.stack.pop()

    def top(self) -> int:
        if not self.stack:  # 栈为空
            return

        x, _ = self.stack[-1]
        return x

    def getMin(self) -> int:
        if not self.stack:  # 栈为空
            return

        _, cur_min_index = self.stack[-1]
        cur_min, _ = self.stack[cur_min_index]
        return cur_min
