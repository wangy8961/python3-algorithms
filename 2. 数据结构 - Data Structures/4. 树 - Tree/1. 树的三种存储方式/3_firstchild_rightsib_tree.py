class FTNodeExist(Exception):
    '''异常: 节点已存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FTNodeNotExist(Exception):
    '''异常: 节点不存在'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FTNode:
    def __init__(self, data):
        self.data = data  # 节点的数据域
        self.firstchild = None  # 节点的第一个孩子
        self.rightsib = None  # 节点的右兄弟

    def __repr__(self):
        return 'Node({!r})'.format(self.data)


class FTree:
    '''使用 “孩子兄弟表示法” 来存储和表示多叉树
    任意树，用 "孩子兄弟表示法" 可以转换成二叉树。再将空节点补齐后就形成了 "扩展二叉树"
    此时，用一种遍历序列（比如，前序遍历的序列）就可以确定整棵二叉树的结构！
    '''
    def __init__(self, pre_list):
        '''创建任意二叉树'''
        if pre_list:
            self.root = self._pre_order_create(pre_list)
        else:
            print('传入了空列表，创建空的二叉树！')
            self.root = None

    def _pre_order_create(self, pre_list, node=None):
        '''深度优先，需要传入 "扩展二叉树" 的前序遍历的列表
        二叉树的节点不一定左、右子树都存在，所以将缺少的 "空节点" 假设用虚拟节点补齐的话，
        补齐后的二叉树称为原二叉树的扩展二叉树
             A
            / \
           B   C
            \
             D

        扩展二叉树:
              A
            /    \
           B      C
          / \    /  \
        '#'  D  '#'  '#'
            / \
          '#' '#'
        '''
        if pre_list:  # 当列表不为空时，表示整棵二叉树还没完全创建完成。当列表为空时，函数隐式返回 None 给上层调用
            data = pre_list.pop(0)
            if data == '#':
                return  # 退出递归的条件，并返回 None 给上层调用
            else:
                node = FTNode(data)  # node 为每棵树（或者子树）的根节点
                node.firstchild = self._pre_order_create(pre_list, node.firstchild)
                node.rightsib = self._pre_order_create(pre_list, node.rightsib)
                return node  # 这里必须返回节点给上层递归调用

    def travel_by_level(self):
        '''树遍历：广度优先，使用队列实现
        按层输出树的节点，即输出一层的节点后，换行，再输出下一层的节点：
        Node('A')
        Node('B')
        Node('D') Node('C')
        Node('G') Node('E')
        Node('H') Node('J') Node('F')
        Node('I')

        如何实现：
        last: 表示正在打印的当前行的最右节点
        nlast: 表示下一行的最右节点

        nlast 一直跟踪记录 '最新' 加入队列的节点即可，因为 '最新' 加入队列的节点一定是目前发现的下一层的最右节点
        '''
        if self.root is None:
            print('这是一棵空树！')
            return

        queue = []  # 模拟队列
        last = self.root  # 开始时，让 last 指向根节点
        queue.append(self.root)  # 首先把根节点加入队列
        while queue:
            cur = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
            print(cur, end=' ')  # 打印当前节点，注意，不换行

            if cur.firstchild is not None:
                queue.append(cur.firstchild)
                nlast = cur.firstchild  # 加入左节点时，让 nlast 指向左节点

            if cur.rightsib is not None:
                queue.append(cur.rightsib)
                nlast = cur.rightsib  # 加入右节点时，让 nlast 指向右节点

            if last == cur:  # 如果 last 与当前弹出的节点相同时，说明该换行了
                last = nlast
                print('')  # 打印换行

    def children(self, data):
        if self.root is None:
            raise FTNodeNotExist("节点FTNode('{}')不存在，因为这是一棵空树！".format(data))

        # 首先要找到这个节点
        node = None

        queue = []  # 模拟队列
        queue.append(self.root)  # 先把根节点加入队列
        while queue:
            cur = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）

            if cur.data == data:  # 找到这个节点了
                node = cur
                children = []
                if node.firstchild:  # 如果第一个孩子都不存在，则该节点没有孩子

                    def dfs_travel(rsib):
                        '''深度优先遍历，使用递归实现'''
                        if rsib is None:  # 递归的终止条件
                            return
                        children.append(rsib)
                        dfs_travel(rsib.rightsib)  # 如果当前节点没有右兄弟，则传入的是None，会终止递归

                    child = node.firstchild  # child 初始时，指向第一个孩子。比如node是节点D，则child是节点G
                    dfs_travel(child)

                return children
            else:
                if cur.firstchild is not None:
                    queue.append(cur.firstchild)
                if cur.rightsib is not None:
                    queue.append(cur.rightsib)

        if not node:
            raise FTNodeNotExist("节点FTNode('{}')不存在".format(data))


if __name__ == '__main__':
    # 创建二叉树
    pre_list = ['A', 'B', 'D', 'G', '#', 'H', '#', 'I', '#', '#', '#', 'C', 'E', 'J', '#', '#', 'F', '#', '#', '#']
    t = FTree(pre_list)

    # 广度优先遍历，且按层输出
    print('*' * 20 + ' 广度优先(按层打印): ' + '*' * 20)
    t.travel_by_level()

    # 获取任意节点的子节点
    print('*' * 20 + ' 获取任意节点的子节点: ' + '*' * 20)
    data = 'D'
    print("节点CTNode('{}')的子节点为: {}".format(data, t.children(data)))

    # Output:
    # ******************** 广度优先(按层打印): ********************
    # Node('A')
    # Node('B')
    # Node('D') Node('C')
    # Node('G') Node('E')
    # Node('H') Node('J') Node('F')
    # Node('I')
    # ******************** 获取任意节点的子节点: ********************
    # 节点CTNode('D')的子节点为: [Node('G'), Node('H'), Node('I')]
