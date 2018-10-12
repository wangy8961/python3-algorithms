class PTNodeExist(Exception):
    '''异常: 节点已存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PTNodeNotExist(Exception):
    '''异常: 节点不存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PTNode:
    def __init__(self, data, parent=-1):
        self.data = data  # 节点的数据域
        self.parent = parent  # 节点的指针域，表示节点的双亲节点的下标。由于根节点没有双亲节点，所以它的parent = -1

    def __repr__(self):
        return 'PTNode({!r}, {!r})'.format(self.data, self.parent)


class PTree:
    '''使用 “双亲表示法” 来存储和表示多叉树'''
    def __init__(self):
        self.__list = []

    def add(self, data, parent):
        '''添加节点'''
        node = PTNode(data, parent)

        if parent == -1:  # 要添加根节点
            if not self.__list:  # 首先判断是否为空树
                print('Info: 节点{}是根节点，它没有双亲节点'.format(node))
                self.__list.append(node)
                print('Info: 节点{}的下标为{}'.format(node, 0))
            else:
                raise PTNodeExist('树已经有根节点了，不能再添加节点{}'.format(node))
        else:
            try:
                print('Info: 节点{}的双亲节点的数据域为{}'.format(node, self.__list[parent].data))
                self.__list.append(node)
                print('Info: 节点{}的下标为{}'.format(node, self.__list.index(node)))
            except IndexError as e:
                raise PTNodeNotExist('节点{}的双亲节点不存在，非法插入'.format(node))

    def parent(self, node):
        '''获取节点的父节点'''
        flag = False  # 要查询的节点 node 是否在树中，不能直接用列表的 if node in self.__list 判断，因为是不同的对象ID
        for item in self.__list:
            if item.data == node.data and item.parent == node.parent:
                flag = True
                break

        if not flag:
            raise PTNodeNotExist('节点{}不存在'.format(node))
        
        if node.parent == -1:
            print('Info: 节点{}是根节点，它没有双亲节点'.format(node))
            return None
        else:
            return self.__list[node.parent]            

    def children(self, node):
        '''获取节点的所有子节点'''
        flag = False
        node_index = None  # 如果要查询的节点 node 在树中，它的下标是多少
        for item in self.__list:
            if item.data == node.data and item.parent == node.parent:  # 说明 item 就是要查询的节点，它存在于树中
                flag = True
                node_index = self.__list.index(item)
                break

        if not flag:
            raise PTNodeNotExist('节点{}不存在'.format(node))

        # 再次遍历整棵树，判断每个节点的 parent 是否是 node 的下标
        return [child for child in self.__list if child.parent == node_index]


if __name__ == '__main__':
    t = PTree()
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
    node = PTNode('B', 0)
    print('节点{}的双亲节点为: {}'.format(node, t.parent(node)))
    print('*' * 50)

    # 获取任意节点的子节点
    node = PTNode('D', 1)
    print('节点{}的子节点为: {}'.format(node, t.children(node)))

    # Output:
    # Info: 节点PTNode('A', -1)是根节点，它没有双亲节点
    # Info: 节点PTNode('A', -1)的下标为0
    # **************************************************
    # Info: 节点PTNode('B', 0)的双亲节点的数据域为A
    # Info: 节点PTNode('B', 0)的下标为1
    # **************************************************
    # Info: 节点PTNode('C', 0)的双亲节点的数据域为A
    # Info: 节点PTNode('C', 0)的下标为2
    # **************************************************
    # Info: 节点PTNode('D', 1)的双亲节点的数据域为B
    # Info: 节点PTNode('D', 1)的下标为3
    # **************************************************
    # Info: 节点PTNode('E', 2)的双亲节点的数据域为C
    # Info: 节点PTNode('E', 2)的下标为4
    # **************************************************
    # Info: 节点PTNode('F', 2)的双亲节点的数据域为C
    # Info: 节点PTNode('F', 2)的下标为5
    # **************************************************
    # Info: 节点PTNode('G', 3)的双亲节点的数据域为D
    # Info: 节点PTNode('G', 3)的下标为6
    # **************************************************
    # Info: 节点PTNode('H', 3)的双亲节点的数据域为D
    # Info: 节点PTNode('H', 3)的下标为7
    # **************************************************
    # Info: 节点PTNode('I', 3)的双亲节点的数据域为D
    # Info: 节点PTNode('I', 3)的下标为8
    # **************************************************
    # Info: 节点PTNode('J', 4)的双亲节点的数据域为E
    # Info: 节点PTNode('J', 4)的下标为9
    # **************************************************
    # 节点PTNode('B', 0)的双亲节点为: PTNode('A', -1)
    # **************************************************
    # 节点PTNode('D', 1)的子节点为: [PTNode('G', 3), PTNode('H', 3), PTNode('I', 3)]
