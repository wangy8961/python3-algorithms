"""
方法二：

解题思路：
只用一个栈，每次压栈时，将 (x, 栈内最小值) 一起压栈

复杂度分析：
时间复杂度：所有操作，时间复杂度均为 O(1)。因为栈的插入、删除与读取操作都是 O(1)，我们定义的每个操作最多调用栈操作一次。
空间复杂度：O(n)，元组 (x, 栈内最小值) 的大小是 x 的两倍。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:  # 栈为空
            self.stack.append((x, x))
        else:
            _, cur_min = self.stack[-1]  # 元组解包
            self.stack.append((x, min(x, cur_min)))
            # 或者:
            # cur_min = self.getMin()
            # self.stack.append((x, min(x, cur_min)))

    def pop(self) -> None:
        if not self.stack:  # 栈为空
            return

        self.stack.pop()

    def top(self) -> int:
        if not self.stack:  # 栈为空
            return

        x, _ = self.stack[-1]  # 元组解包
        return x

    def getMin(self) -> int:
        if not self.stack:  # 栈为空
            return

        _, cur_min = self.stack[-1]  # 元组解包
        return cur_min
