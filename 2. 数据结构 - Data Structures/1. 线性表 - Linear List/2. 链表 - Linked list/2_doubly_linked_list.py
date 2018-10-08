class Node:
    '''双向链表的节点'''
    def __init__(self, value):
        self.value = value  # 节点的信息域
        self.prev = None    # 指针域，指向前驱节点
        self.next = None    # 指针域，指向后继节点

    def __repr__(self):
        return 'Node({!r})'.format(self.value)


class DoublyLinkedList:
    def __init__(self, node=None):
        '''创建一个双向链表对象时，如果不传入头节点，则创建空链表'''
        self.__head = node

    def is_empty(self):
        '''判断是否为空链表'''
        return self.__head is None

    def length(self):
        '''求链表的长度'''
        cur = self.__head  # 游标，用来表示当前节点
        count = 0  # 用来统计已遍历的节点数目

        # 1. 如果是空链表，self.__head为None，则cur为None，不会进入循环体，最后返回 count = 0，符合
        # 2. 如果不是空链表，当cur移动到尾节点时，cur.next 是None，循环体中的 cur = cur.next 会让 cur = None，继续往后移动时会退出循环
        while cur is not None:
            count += 1
            cur = cur.next  # 向后移动游标

        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head  # 游标，用来表示当前节点
        while cur is not None:
            yield cur.value  # 生成当前节点的值
            cur = cur.next  # 向后移动游标

    def append(self, value):
        '''在链表的尾部添加节点。注意：传入的 value 是节点的值'''
        node = Node(value)

        if self.is_empty():  # 如果是空链表
            self.__head = node
        else:
            cur = self.__head  # 游标，用来表示当前节点
            # 遍历链表，直到找到了尾节点后，退出循环
            while cur.next is not None:
                cur = cur.next
            # 此时，cur 表示尾节点
            cur.next = node  # 将尾节点的 next 指向新增节点
            node.prev = cur  # 将新增节点的 prev 指向尾节点

    def head_add(self, value):
        '''在链表的头部添加节点'''
        node = Node(value)

        if self.is_empty():  # 如果是空链表
            self.__head = node
        else:
            node.next = self.__head  # 1. 将新增节点的 next 指向原来的头节点
            node.next.prev = node  # 2. 再将原来的头节点的 prev 指向新增节点
            self.__head = node  # 3. 最后将链表的 __head 属性指向新增节点即可

    def insert(self, pos, value):
        '''在指定位置添加节点。 pos 表示节点的下标，为了跟列表等一样，这里规定 pos 从0开始计数，即头节点的 pos 为0'''
        if pos <= 0:  # 暂时不支持负数的下标。如果传入负数或者0，统一在头部插入
            self.head_add(value)
        elif pos > self.length() - 1:  # 如果传入的下标大于链表的长度减去1，默认使用在尾部插入
            self.append(value)
        else:
            cur = self.__head  # 游标，用来表示 pos 位置的节点
            count = 0
            while count < pos:  # 当count = pos 时，表示已经找到了 pos 的节点，退出循环
                count += 1
                cur = cur.next  # 向后移动游标
            # 退出循环后，cur 指向 pos 所在的节点
            node = Node(value)
            node.next = cur  # 1. 将新增节点的 next 指向 cur
            node.prev = cur.prev  # 2. 将新增节点的 prev 指向 cur 的前驱节点
            cur.prev.next = node  # 3. 将 cur 的前驱节点的 next 重新指向新增节点
            cur.prev = node  # 4. 将 cur 的 prev 重新指向新增节点

    def search(self, value):
        '''查找指定的元素值是否在链表中，也适合空链表的情况'''
        cur = self.__head
        while cur is not None:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False  # 遍历完整个链表也没找到时

    def remove(self, value):
        '''在链表中删除指定元素值，跟列表中的 remove() 类似，也是删除第一个遇到的元素'''
        cur = self.__head

        while cur is not None:  # 向后遍历链表
            if cur.value == value:  # 表示找到了要删除的节点，此时，cur 指向要删除的节点
                if cur.prev is None:  # 特殊情况1： 如果要删除的节点是头节点时
                    if cur.next is None:  # 特殊情况2： 链表只有一个节点，刚好它就是要删除的节点，此时 cur.next 是 None
                        self.__head = None  # 变回空链表
                    else:  # 链表不只一个节点
                        self.__head = cur.next
                        cur.next.prev = None  # 将 cur 的后继节点的 prev 重新指向 None，因为它现在是新的头节点了
                elif cur.next is None:  # 特殊情况3： 如果要删除的节点是尾节点时，cur.next是None
                    cur.prev.next = None
                else:
                    cur.prev.next = cur.next  # 1. 将 cur 的前驱节点的 next 重新指向 cur 的后继节点
                    cur.next.prev = cur.prev  # 2. 将 cur 的后继节点的 prev 重新指向 cur 的前驱节点，这样 cur 就从双向链表中退出来了

                # 当找到要删除的节点时，需要退出 while 循环
                break
            else:
                cur = cur.next  # 向后移动


if __name__ == '__main__':
    # 创建空链表
    doubly_linked_list = DoublyLinkedList()
    print('*' * 20 + ' 空链表时: ' + '*' * 20)
    print('是否为空链表: ', doubly_linked_list.is_empty())
    print('链表的长度: ', doubly_linked_list.length())

    # 在尾部添加一些节点
    doubly_linked_list.append(10)
    doubly_linked_list.append('Python')
    doubly_linked_list.append(23.50)
    print('*' * 20 + ' 在尾部添加一些节点后: ' + '*' * 20)
    print('是否为空链表: ', doubly_linked_list.is_empty())
    print('链表的长度: ', doubly_linked_list.length())
    # 遍历链表
    gen = doubly_linked_list.travel()
    for i in gen:
        print(i, end=' ')

    # 在头部添加节点
    doubly_linked_list.head_add('Hello')
    print('')  # 换行
    print('*' * 20 + ' 在头部添加节点后: ' + '*' * 20)
    gen = doubly_linked_list.travel()
    for i in gen:
        print(i, end=' ')

    # 在指定位置添加节点
    doubly_linked_list.insert(2, 100)
    # doubly_linked_list.insert(-1, 100)  # 测试 pos 为负数的情况
    # doubly_linked_list.insert(10, 100)  # 测试 pos 下标越界的情况
    print('')  # 换行
    print('*' * 20 + ' 在指定位置插入节点后: ' + '*' * 20)
    gen = doubly_linked_list.travel()
    for i in gen:
        print(i, end=' ')

    # 查看元素是否在链表中
    item = 100
    # item = 200  # 测试
    print('')  # 换行
    print('*' * 20 + ' 查看元素是否在链表中: ' + '*' * 20)
    print('{} 是否在链表中: {}'.format(item, doubly_linked_list.search(item)))

    # 在链表中删除指定元素值
    print('*' * 20 + ' 在链表中删除指定元素值: ' + '*' * 20)
    doubly_linked_list.remove(100)
    # doubly_linked_list.remove('Hello')  # 测试：要删除的元素刚好是头节点
    # doubly_linked_list.remove(23.5)  # 测试：要删除的元素刚好是头节点
    gen = doubly_linked_list.travel()
    for i in gen:
        print(i, end=' ')

    # Output:
    # ******************** 空链表时: ********************
    # 是否为空链表:  True
    # 链表的长度:  0
    # ******************** 在尾部添加一些节点后: ********************
    # 是否为空链表:  False
    # 链表的长度:  3
    # 10 Python 23.5
    # ******************** 在头部添加节点后: ********************
    # Hello 10 Python 23.5
    # ******************** 在指定位置插入节点后: ********************
    # Hello 10 100 Python 23.5
    # ******************** 查看元素是否在链表中: ********************
    # 100 是否在链表中: True
    # ******************** 在链表中删除指定元素值: ********************
    # Hello 10 Python 23.5
