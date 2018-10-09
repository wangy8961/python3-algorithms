class Deque:
    '''用顺序表实现双端队列'''
    def __init__(self):
        self.__list = []  # 用来存放元素的容器，这里使用列表（顺序表）

    def is_empty(self):
        '''判断双端队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回双端队列的元素个数'''
        return len(self.__list)

    def append(self, value):
        '''尾部插入'''
        self.__list.append(value)

    def appendleft(self, value):
        '''头部插入'''
        self.__list.insert(0, value)

    def pop(self):
        '''尾部删除'''
        return self.__list.pop()

    def popleft(self):
        '''头部删除'''
        return self.__list.pop(0)


if __name__ == '__main__':
    # 创建空双端队列
    q = Deque()
    print('*' * 20 + ' 空双端队列时: ' + '*' * 20)
    print('是否为空双端队列: ', q.is_empty())
    print('双端队列的元素个数: ', q.size())

    # 尾部插入一些元素
    q.append(10)
    q.append('Python')
    q.append(23.50)
    print('*' * 20 + ' 尾部插入一些元素后: ' + '*' * 20)
    print('是否为空双端队列: ', q.is_empty())
    print('双端队列的元素个数: ', q.size())

    # 尾部删除
    print('*' * 20 + ' 尾部删除（后进先出）: ' + '*' * 20)
    print(q.pop())
    print('双端队列的元素个数: ', q.size())

    # 头部插入一些元素
    q.appendleft('Hello')
    q.appendleft('100')
    print('*' * 20 + ' 头部插入一些元素后: ' + '*' * 20)
    print('双端队列的元素个数: ', q.size())

    # 头部删除
    print('*' * 20 + ' 头部删除（后进先出）: ' + '*' * 20)
    print(q.popleft())
    print('双端队列的元素个数: ', q.size())

    # Output:
    # ******************** 空双端队列时: ********************
    # 是否为空双端队列:  True
    # 双端队列的元素个数:  0
    # ******************** 尾部插入一些元素后: ********************
    # 是否为空双端队列:  False
    # 双端队列的元素个数:  3
    # ******************** 尾部删除（后进先出）: ********************
    # 23.5
    # 双端队列的元素个数:  2
    # ******************** 头部插入一些元素后: ********************
    # 双端队列的元素个数:  4
    # ******************** 头部删除（后进先出）: ********************
    # 100
    # 双端队列的元素个数:  3
