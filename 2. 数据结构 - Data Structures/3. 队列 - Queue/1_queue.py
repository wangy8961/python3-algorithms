class Queue:
    '''用顺序表实现队列'''
    def __init__(self):
        self.__list = []  # 用来存放元素的容器，这里使用列表（顺序表）

    def is_empty(self):
        '''判断队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回队列的元素个数'''
        return len(self.__list)

    def enqueue(self, value):
        '''往队尾插入一个元素
        这里假设队尾是列表的尾部，如果你的队列的 '出队' 操作很频繁，
        则应该设置队尾是列表的头部，这样出队操作是 self.__list.pop()，它的时间复杂度为O(1)
        '''
        self.__list.append(value)

    def dequeue(self):
        '''从队头删除一个元素'''
        return self.__list.pop(0)


if __name__ == '__main__':
    # 创建空队列
    q = Queue()
    print('*' * 20 + ' 空队列时: ' + '*' * 20)
    print('是否为空队列: ', q.is_empty())
    print('队列的元素个数: ', q.size())

    # 队尾插入一些元素
    q.enqueue(10)
    q.enqueue('Python')
    q.enqueue(23.50)
    q.enqueue('Hello')
    q.enqueue(100)
    print('*' * 20 + ' 队尾插入一些元素后: ' + '*' * 20)
    print('是否为空队列: ', q.is_empty())
    print('队列的元素个数: ', q.size())

    # 队头删除一些元素
    print('*' * 20 + ' 元素按入队的顺序依次出队: ' + '*' * 20)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    # Output:
    # ******************** 空队列时: ********************
    # 是否为空队列:  True
    # 队列的元素个数:  0
    # ******************** 队尾插入一些元素后: ********************
    # 是否为空队列:  False
    # 队列的元素个数:  5
    # ******************** 元素按入队的顺序依次出队: ********************
    # 10
    # Python
    # 23.5
    # Hello
    # 100
