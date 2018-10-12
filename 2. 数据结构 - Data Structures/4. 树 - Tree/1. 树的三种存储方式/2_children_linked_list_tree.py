from utils.singly_linked_list import SinglyLinkedList


class CTNodeExist(Exception):
    '''异常: 节点已存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CTNodeNotExist(Exception):
    '''异常: 节点不存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CTNode:
    def __init__(self, data):
        self.data = data  # 节点的数据域
        self.children = SinglyLinkedList()  # 节点的子节点组成的单链表

    def __repr__(self):
        return 'CTNode({!r})'.format(self.data)


class CTree:
    '''使用 “孩子表示法” 来存储和表示多叉树'''
    def __init__(self):
        self.__list = []

    def add(self, data, parent):
        '''添加节点
        @param data: 节点的数据域
        @param parent: 节点的父节点的下标
        '''
        node = CTNode(data)

        if parent == -1:  # 要添加根节点
            if not self.__list:
                print('Info: 节点{}是根节点，它没有双亲节点'.format(node))
                self.__list.append(node)
                print('Info: 节点{}的下标为{}'.format(node, 0))
            else:
                raise CTNodeExist('树已经有根节点了，不能再添加节点{}'.format(node))
        else:
            try:
                print('Info: 节点{}的双亲节点的数据域为{}'.format(node, self.__list[parent].data))
                self.__list.append(node)
                node_index = self.__list.index(node)  # 新添加节点的下标
                print('Info: 节点{}的下标为{}'.format(node, node_index))
                self.__list[parent].children.append(node_index)
            except IndexError as e:
                raise CTNodeNotExist('节点{}的双亲节点不存在，非法插入'.format(node))

    def parent(self, data):
        '''获取节点的父节点'''
        node = None  # 要查询的节点是哪个
        for i in self.__list:
            if i.data == data:  # 说明 i 就是要查询的节点，它存在于树中
                node = i
                break

        if not node:
            raise CTNodeNotExist("节点CTNode('{}')不存在".format(data))

        node_index = self.__list.index(node)
        if node_index == 0:
            print('Info: 节点{}是根节点，它没有双亲节点'.format(node))
            return None
        else:
            for j in self.__list:
                if j.children.search(node_index):  # 如果在 j 的孩子单链表中找到了包含下标 node_index ，则表示 node 节点是 j 的子节点
                    return j

    def children(self, data):
        '''获取节点的所有子节点'''
        node = None  # 要查询的节点是哪个
        for i in self.__list:
            if i.data == data:  # 说明 i 就是要查询的节点，它存在于树中
                node = i
                gen = node.children.travel()  # 遍历孩子单链表
                return [self.__list[j] for j in gen]

        if not node:
            raise CTNodeNotExist("节点CTNode('{}')不存在".format(data))


if __name__ == '__main__':
    t = CTree()
    t.add('A', -1)
    print('*' * 50)

    t.add('B', 0)
    print('*' * 50)

    t.add('C', 0)
    print('*' * 50)

    t.add('D', 1)
    print('*' * 50)

    t.add('E', 2)
    print('*' * 50)

    t.add('F', 2)
    print('*' * 50)

    t.add('G', 3)
    print('*' * 50)

    t.add('H', 3)
    print('*' * 50)

    t.add('I', 3)
    print('*' * 50)

    t.add('J', 4)
    print('*' * 50)

    # 获取任意节点的父节点
    data = 'B'
    print("节点CTNode('{}')的双亲节点为: {}".format(data, t.parent(data)))
    print('*' * 50)

    # 获取任意节点的子节点
    data = 'D'
    print("节点CTNode('{}')的子节点为: {}".format(data, t.children(data)))

    # Output:
    # Info: 节点CTNode('A')是根节点，它没有双亲节点
    # Info: 节点CTNode('A')的下标为0
    # **************************************************
    # Info: 节点CTNode('B')的双亲节点的数据域为A
    # Info: 节点CTNode('B')的下标为1
    # **************************************************
    # Info: 节点CTNode('C')的双亲节点的数据域为A
    # Info: 节点CTNode('C')的下标为2
    # **************************************************
    # Info: 节点CTNode('D')的双亲节点的数据域为B
    # Info: 节点CTNode('D')的下标为3
    # **************************************************
    # Info: 节点CTNode('E')的双亲节点的数据域为C
    # Info: 节点CTNode('E')的下标为4
    # **************************************************
    # Info: 节点CTNode('F')的双亲节点的数据域为C
    # Info: 节点CTNode('F')的下标为5
    # **************************************************
    # Info: 节点CTNode('G')的双亲节点的数据域为D
    # Info: 节点CTNode('G')的下标为6
    # **************************************************
    # Info: 节点CTNode('H')的双亲节点的数据域为D
    # Info: 节点CTNode('H')的下标为7
    # **************************************************
    # Info: 节点CTNode('I')的双亲节点的数据域为D
    # Info: 节点CTNode('I')的下标为8
    # **************************************************
    # Info: 节点CTNode('J')的双亲节点的数据域为E
    # Info: 节点CTNode('J')的下标为9
    # **************************************************
    # 节点CTNode('B')的双亲节点为: CTNode('A')
    # **************************************************
    # 节点CTNode('D')的子节点为: [CTNode('G'), CTNode('H'), CTNode('I')]
