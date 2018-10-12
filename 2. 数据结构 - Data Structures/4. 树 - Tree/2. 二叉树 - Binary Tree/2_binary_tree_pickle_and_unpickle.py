import os


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
        self.pickle_str = ''  # 序列化后的字符串

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

    def pre_order_traversal(self, cur):
        '''树的遍历：深度优先，使用递归实现
        前序遍历: 根、左、右
        '''
        if cur is None:  # 递归的终止条件
            return

        print(cur, end=' ')
        self.pre_order_traversal(cur.lchild)  # 如果当前节点(叶子节点)没有左孩子，则传入的是None，会终止递归
        self.pre_order_traversal(cur.rchild)

    def pickling(self):
        '''序列化：内存中的二叉树数据结构 --> 文件中的字符串
        方式：
        1. 根据先序遍历序列化
        2. 根据中序遍历序列化
        3. 根据后序遍历序列化
        4. 根据广度优先遍历(按层)序列化

        这里使用先序遍历(根、左、右)对二叉树进行序列化，主要步骤为：
        1. 假设序列化的结果为 s，初始化 s 为空字符串
        2. 先序遍历二叉树时，如果遇到空节点(比如叶子节点的左、右节点为null)，就在字符串 s 的末尾添加 '#!'
        其中，# 表示这是空节点，! 表示节点值的结束标志
        3. 如果遇到不为空的节点时，假设节点值为3，就在字符串 s 的末尾添加 '3!'

        为什么需要用 ! 表示节点值的结束标志？
             12                 1
            /  \               /  \
           3   null           23   null
          /  \               /  \
        null  null     和  null  null

        都是 '123###' ，就会产生歧义，但是明显它们是两棵不同的树。使用 ! 表示的正确结果是：
        第1棵树： '12!3!#!#!#!'
        第2棵树： '1!23!#!#!#!'
        '''
        self.pickle_str = ''  # 每次调用本序列化方法时，先清空字符串
        self._pre_order_pickling(self.root)

        basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录
        with open(os.path.join(basepath, 'pickle_result.txt'), 'w') as f:
            f.write(self.pickle_str)

        return self.pickle_str

    def _pre_order_pickling(self, cur):
        '''树的遍历：深度优先，使用递归实现
        先序遍历: 根、左、右
        '''
        if cur is None:  # 递归的终止条件
            self.pickle_str += '#!'
            return

        self.pickle_str = self.pickle_str + str(cur.data) + '!'
        self._pre_order_pickling(cur.lchild)  # 如果当前节点(叶子节点)没有左节点，则传入的是None，会终止递归
        self._pre_order_pickling(cur.rchild)

    @classmethod
    def unpickling(self, filename):
        '''反序列化：文件中的字符串 --> 内存中的二叉树数据结构'''
        with open(filename, 'r') as f:
            result = f.read()

        # ['0', '1', '3', '7', '#', '#', '8', '#', '#', '4', '9', '#', '#', '#', '2', '5', '#', '#', '6', '#', '#', '']
        values = result.split('!')
        # 移除最后一个元素：''  注意不能 remove('')，因为可能添加节点时，就是添加binary_tree.breadth_first_add('')
        del values[-1]

        binary_tree = BinaryTree()  # 创建空树
        binary_tree.root = binary_tree._pre_order_create(values)  # 传入前序遍历序列，创建二叉树

        return binary_tree

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
                node = Node(data)  # node 为每棵树（或者子树）的根节点
                node.lchild = self._pre_order_create(pre_list, node.lchild)
                node.rchild = self._pre_order_create(pre_list, node.rchild)
                return node  # 这里必须返回节点给上层递归调用


if __name__ == '__main__':
    binary_tree = BinaryTree()  # 创建空树
    binary_tree.add('A')  # 添加根节点
    binary_tree.add('B')
    binary_tree.add('C')
    binary_tree.add('D')
    binary_tree.add('E')
    binary_tree.add('F')
    binary_tree.add('G')
    binary_tree.add('H')
    binary_tree.add('I')
    binary_tree.add('J')

    # 序列化
    print('*' * 20 + ' 序列化: ' + '*' * 20)
    print('按 "前序遍历" 序列化后的字符串: ', binary_tree.pickling())

    # 反序列化
    print('*' * 20 + ' 反序列化（前序遍历）: ' + '*' * 20)
    basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录
    filename = os.path.join(basepath, 'pickle_result.txt')
    t = BinaryTree.unpickling(filename)
    t.pre_order_traversal(t.root)

    # Output:
    # ******************** 序列化: ********************
    # 按 "前序遍历" 序列化后的字符串:  A!B!D!H!#!#!I!#!#!E!J!#!#!#!C!F!#!#!G!#!#!
    # ******************** 反序列化（前序遍历）: ********************
    # Node('A') Node('B') Node('D') Node('H') Node('I') Node('E') Node('J') Node('C') Node('F') Node('G')
