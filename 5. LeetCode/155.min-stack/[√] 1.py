"""
方法一：两个栈

解题思路：
可以使用一个辅助栈，与元素栈同步插入与删除，用于存储与每个元素对应的最小值
1. 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
2. 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
3. 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中

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
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:  # 栈为空
            self.min_stack.append(x)
        else:
            # min_element = self.min_stack[-1]
            # if x < min_element:
            #     self.min_stack.append(x)
            # else:
            #     self.min_stack.append(min_element)
            # 等价于上面的5行代码
            self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.stack or not self.min_stack:  # 栈为空
            return

        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:  # 栈为空
            return

        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:  # 栈为空
            return

        return self.min_stack[-1]
