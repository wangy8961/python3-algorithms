"""
解题思路：
队列是一种「先进先出(first in - first out, FIFO)」的数据结构，队列中的元素都从后端(rear)入队(push)，从前端(front)出队(pop)。
实现队列的三种方法：
- 数组(顺序队列)
- 链表(链式队列)
- 两个栈

栈是一种「后进先出(last in - first out, LIFO)」的数据结构，栈中元素从栈顶(top)压入(push)，也从栈顶弹出(pop)。
为了满足队列的 FIFO 的特性，我们需要用到两个栈，用它们其中一个来反转元素的入队顺序，用另一个来存储元素的最终顺序。


要点：
1. 入队 push()
任何情况下，都只需要直接压入栈1即可

2. 出队 pop() / 返回队首元素 peek()
只有栈2为空时，才依次将栈1的元素弹出并压入栈2中！然后再对栈2执行 pop() 或 peek()
如果栈2不为空，直接对栈2执行 pop() 或 peek()。此时绝对不允许任何元素再压入栈2，否则就会「后进先出」了，与队列的特性「先进先出」相违背


复杂度分析：
1. push()
时间复杂度：O(1)。向栈压入元素的时间复杂度为 O(1)
空间复杂度：O(1)

2. pop()
时间复杂度：均摊时间复杂度为 O(1)，最坏时间复杂度为 O(n)。在最坏情况下，s2 为空，算法需要从 s1 中弹出 n 个元素，然后再把这 n 个元素压入 s2，在这里 n 代表队列的大小。这个过程产生了 2n 次操作，时间复杂度为 O(n)。但当 s2 非空时，算法就只有 O(1) 的时间复杂度。所以，使用均摊时间复杂度为 O(1)
空间复杂度：O(1)

3. peek()
时间复杂度：均摊时间复杂度为 O(1)，最坏时间复杂度为 O(n)。在最坏情况下，s2 为空，算法需要从 s1 中弹出 n 个元素，然后再把这 n 个元素压入 s2，在这里 n 代表队列的大小。这个过程产生了 2n 次操作，时间复杂度为 O(n)。但当 s2 非空时，算法就只有 O(1) 的时间复杂度。所以，使用均摊时间复杂度为 O(1)
空间复杂度：O(1)

4. empty()
时间复杂度：O(1)
空间复杂度：O(1)
"""


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []  # 用来存放栈元素的容器，这里使用列表 (顺序栈)。还可以使用链表实现栈 (链式栈)

    def __str__(self):
        return str(self.items)

    def push(self, x: int) -> None:
        """
        Push element x to the top of stack.
        """
        self.items.append(x)

    def pop(self) -> int:
        """
        Removes the element from the top of stack and returns that element.
        """
        return self.items.pop()

    def peek(self):
        """
        Get the top element.
        """
        if self.items:  # 栈不为空时
            return self.items[-1]
        else:
            return None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.items) == 0


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = MyStack()  # 栈1
        self.s2 = MyStack()  # 栈2

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)  # 只需压入栈1即可

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2.empty():  # 如果栈2为空，先将栈1的元素依次弹出并压入栈2中
            while not self.s1.empty():
                item = self.s1.pop()
                self.s2.push(item)
        return self.s2.pop()  # 弹出栈2的栈顶元素

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2.empty():
            while not self.s1.empty():  # 先将栈1的元素依次弹出并压入栈2中
                item = self.s1.pop()
                self.s2.push(item)
        return self.s2.peek()  # 返回栈顶元素

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s1.empty() and self.s2.empty()  # 当栈1和栈2都为空时，队列才为空


def main():
    q = MyQueue()
    assert q.empty() is True
    assert q.peek() is None

    q.push(1)
    q.push(2)
    q.push(3)
    assert q.empty() is False
    assert q.peek() == 1

    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3


if __name__ == '__main__':
    main()
