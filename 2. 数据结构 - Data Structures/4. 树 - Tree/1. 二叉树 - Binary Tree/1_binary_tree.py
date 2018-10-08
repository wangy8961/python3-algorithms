class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self._value = value  # 本节点的值
        self.left_child = left_child  # 本节点的左孩子
        self.right_child = right_child  # 本节点的右孩子

    def __repr__(self):
        return 'Node({!r})'.format(self._value)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def breadth_first_add(self, node_value):
        '''添加节点：广度优先，使用队列实现'''
        node = Node(node_value)
        # 如果树还是空树，则把该节点添加为根节点
        if self.root is None:
            self.root = node
        else:
            queue = []  # 模拟队列
            queue.append(self.root)  # 首先把根节点加入队列
            while queue:
                current_node = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
                if current_node.left_child is None:
                    current_node.left_child = node
                    return
                else:
                    # 如果弹出的节点的左节点不为空，则把它的左节点依次加入队列，继续判断左节点的子节点是否为空
                    queue.append(current_node.left_child)

                if current_node.right_child is None:
                    current_node.right_child = node
                    return
                else:
                    # 如果弹出的节点的右节点不为空，则把它的右节点依次加入队列，继续判断右节点的子节点是否为空
                    queue.append(current_node.right_child)

    def breadth_first_search(self):
        '''树遍历：广度优先，使用队列实现'''
        if self.root is None:
            return

        queue = []  # 模拟队列
        queue.append(self.root)  # 首先把根节点加入队列
        while queue:
            current_node = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
            print(current_node, end=' ')  # 打印当前节点，注意，不换行
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)

    def breadth_first_search2(self):
        '''树遍历：广度优先，使用队列实现
        按层输出树的节点，即输出一层的节点后，换行，再输出下一层的节点：
        Node(0)
        Node(1) Node(2)
        Node(3) Node(4) Node(5) Node(6)
        Node(7) Node(8) Node(9)

        如何实现：
        last: 表示正在打印的当前行的最右节点
        nlast: 表示下一行的最右节点

        nlast 一直跟踪记录 '最新' 加入队列的节点即可，因为 '最新' 加入队列的节点一定是目前发现的下一层的最右节点
        '''
        if self.root is None:
            return

        queue = []  # 模拟队列
        last = self.root  # 开始时，让 last 指向根节点
        queue.append(self.root)  # 首先把根节点加入队列
        while queue:
            current_node = queue.pop(0)  # 弹出队列中的第1个元素（即最先加入队列的元素，先进先出）
            print(current_node, end=' ')  # 打印当前节点，注意，不换行

            if current_node.left_child is not None:
                queue.append(current_node.left_child)
                nlast = current_node.left_child  # 加入左节点时，让 nlast 指向左节点

            if current_node.right_child is not None:
                queue.append(current_node.right_child)
                nlast = current_node.right_child  # 加入右节点时，让 nlast 指向右节点

            if last == current_node:  # 如果 last 与当前弹出的节点相同时，说明该换行了
                last = nlast
                print('')  # 打印换行

    def pre_order_traversal(self, current_node):
        '''树的遍历：深度优先，使用递归实现
        先序遍历: 根、左、右
        '''
        if current_node is None:  # 递归的终止条件
            return

        print(current_node, end=' ')
        self.pre_order_traversal(current_node.left_child)  # 如果当前节点(叶子节点)没有左节点，则传入的是None，会终止递归
        self.pre_order_traversal(current_node.right_child)

    def in_order_traversal(self, current_node):
        '''树的遍历：深度优先，使用递归实现
        中序遍历: 左、根、右
        '''
        if current_node is None:  # 递归的终止条件
            return

        self.in_order_traversal(current_node.left_child)  # 如果当前节点(叶子节点)没有左节点，则传入的是None，会终止递归
        print(current_node, end=' ')
        self.in_order_traversal(current_node.right_child)

    def post_order_traversal(self, current_node):
        '''树的遍历：深度优先，使用递归实现
        后序遍历: 左、右、根
        '''
        if current_node is None:  # 递归的终止条件
            return

        self.post_order_traversal(current_node.left_child)  # 如果当前节点(叶子节点)没有左节点，则传入的是None，会终止递归
        self.post_order_traversal(current_node.right_child)
        print(current_node, end=' ')


if __name__ == '__main__':
    binary_tree = BinaryTree()  # 创建空树
    binary_tree.breadth_first_add(0)  # 添加根节点
    binary_tree.breadth_first_add(1)
    binary_tree.breadth_first_add(2)
    binary_tree.breadth_first_add(3)
    binary_tree.breadth_first_add(4)
    binary_tree.breadth_first_add(5)
    binary_tree.breadth_first_add(6)
    binary_tree.breadth_first_add(7)
    binary_tree.breadth_first_add(8)
    binary_tree.breadth_first_add(9)

    print('*' * 20 + ' 广度优先: ' + '*' * 20)
    binary_tree.breadth_first_search()
    print('')  # 换行

    print('*' * 20 + ' 广度优先(按层打印): ' + '*' * 20)
    binary_tree.breadth_first_search2()

    print('*' * 20 + ' 先序遍历: ' + '*' * 20)
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
    # ******************** 先序遍历: ********************
    # Node(0) Node(1) Node(3) Node(7) Node(8) Node(4) Node(9) Node(2) Node(5) Node(6)
    # ******************** 中序遍历: ********************
    # Node(7) Node(3) Node(8) Node(1) Node(9) Node(4) Node(0) Node(5) Node(2) Node(6)
    # ******************** 后序遍历: ********************
    # Node(7) Node(8) Node(3) Node(9) Node(4) Node(1) Node(5) Node(6) Node(2) Node(0)
