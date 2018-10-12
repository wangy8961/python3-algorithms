class Node:
    def __init__(self, data):
        self.data = data  # 节点的数据域
        self.lchild = None  # 节点的左孩子
        self.rchild = None  # 节点的右孩子

    def __repr__(self):
        return 'Node({!r})'.format(self.data)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        '''添加节点：广度优先，使用队列实现（这种方式是创建了 "完全二叉树"，如果想创建普通二叉树就不行）'''
        node = Node(data)
        # 如果树还是空树，则把该节点添加为根节点
        if self.root is None:
            self.root = node
        else:
            queue = []  # 模拟队列
            queue.append(self.root)  # 首先把根节点加入队列
            while queue:
                cur = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
                if cur.lchild is None:
                    cur.lchild = node
                    return
                else:
                    # 如果弹出的节点的左孩子不为空，则把它的左孩子加入队列，后面继续判断左孩子
                    queue.append(cur.lchild)

                if cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    # 如果弹出的节点的右孩子不为空，则把它的右孩子加入队列，后面继续判断右孩子
                    queue.append(cur.rchild)

    def breadth_first_search(self):
        '''树遍历：广度优先，使用队列实现'''
        if self.root is None:
            return

        queue = []  # 模拟队列
        queue.append(self.root)  # 首先把根节点加入队列
        while queue:
            cur = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
            print(cur, end=' ')  # 打印当前节点，注意，不换行
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

    def breadth_first_search2(self):
        '''树遍历：广度优先，使用队列实现
        按层输出树的节点，即输出一层的节点后，换行，再输出下一层的节点：
        Node(0)
        Node(1) Node(2)
        Node(3) Node(4) Node(5) Node(6)
        Node(7) Node(8) Node(9)

        如何实现：
        last: 表示正在打印的当前行的最右孩子
        nlast: 表示下一行的最右孩子

        nlast 一直跟踪记录 '最新' 加入队列的节点即可，因为 '最新' 加入队列的节点一定是目前发现的下一层的最右孩子
        '''
        if self.root is None:
            return

        queue = []  # 模拟队列
        last = self.root  # 开始时，让 last 指向根节点
        queue.append(self.root)  # 首先把根节点加入队列
        while queue:
            cur = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
            print(cur, end=' ')  # 打印当前节点，注意，不换行

            if cur.lchild is not None:
                queue.append(cur.lchild)
                nlast = cur.lchild  # 加入左孩子时，让 nlast 指向左孩子

            if cur.rchild is not None:
                queue.append(cur.rchild)
                nlast = cur.rchild  # 加入右孩子时，让 nlast 指向右孩子

            if last == cur:  # 如果 last 与当前弹出的节点相同时，说明该换行了
                last = nlast
                print('')  # 打印换行

    def pre_order_traversal(self, cur):
        '''树的遍历：深度优先，使用递归实现
        前序遍历: 根、左、右
        '''
        if cur is None:  # 递归的终止条件
            return

        print(cur, end=' ')
        self.pre_order_traversal(cur.lchild)  # 如果当前节点(叶子节点)没有左孩子，则传入的是None，会终止递归
        self.pre_order_traversal(cur.rchild)

    def in_order_traversal(self, cur):
        '''树的遍历：深度优先，使用递归实现
        中序遍历: 左、根、右
        '''
        if cur is None:  # 递归的终止条件
            return

        self.in_order_traversal(cur.lchild)  # 如果当前节点(叶子节点)没有左孩子，则传入的是None，会终止递归
        print(cur, end=' ')
        self.in_order_traversal(cur.rchild)

    def post_order_traversal(self, cur):
        '''树的遍历：深度优先，使用递归实现
        后序遍历: 左、右、根
        '''
        if cur is None:  # 递归的终止条件
            return

        self.post_order_traversal(cur.lchild)  # 如果当前节点(叶子节点)没有左孩子，则传入的是None，会终止递归
        self.post_order_traversal(cur.rchild)
        print(cur, end=' ')


if __name__ == '__main__':
    binary_tree = BinaryTree()  # 创建空树
    binary_tree.add(0)  # 添加根节点
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    binary_tree.add(7)
    binary_tree.add(8)
    binary_tree.add(9)

    print('*' * 20 + ' 广度优先: ' + '*' * 20)
    binary_tree.breadth_first_search()
    print('')  # 换行

    print('*' * 20 + ' 广度优先(按层打印): ' + '*' * 20)
    binary_tree.breadth_first_search2()

    print('*' * 20 + ' 前序遍历: ' + '*' * 20)
    binary_tree.pre_order_traversal(binary_tree.root)
    print('')  # 换行

    print('*' * 20 + ' 中序遍历: ' + '*' * 20)
    binary_tree.in_order_traversal(binary_tree.root)
    print('')  # 换行

    print('*' * 20 + ' 后序遍历: ' + '*' * 20)
    binary_tree.post_order_traversal(binary_tree.root)

    # Output:
    # ******************** 广度优先: ********************
    # Node(0) Node(1) Node(2) Node(3) Node(4) Node(5) Node(6) Node(7) Node(8) Node(9)
    # ******************** 广度优先(按层打印): ********************
    # Node(0)
    # Node(1) Node(2)
    # Node(3) Node(4) Node(5) Node(6)
    # Node(7) Node(8) Node(9)
    # ******************** 前序遍历: ********************
    # Node(0) Node(1) Node(3) Node(7) Node(8) Node(4) Node(9) Node(2) Node(5) Node(6)
    # ******************** 中序遍历: ********************
    # Node(7) Node(3) Node(8) Node(1) Node(9) Node(4) Node(0) Node(5) Node(2) Node(6)
    # ******************** 后序遍历: ********************
    # Node(7) Node(8) Node(3) Node(9) Node(4) Node(1) Node(5) Node(6) Node(2) Node(0)
