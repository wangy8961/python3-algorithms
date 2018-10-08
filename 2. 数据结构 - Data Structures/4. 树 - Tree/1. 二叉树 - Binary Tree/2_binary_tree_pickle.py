import os


class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value  # 本节点的值
        self.left_child = left_child  # 本节点的左孩子
        self.right_child = right_child  # 本节点的右孩子

    def __repr__(self):
        return 'Node({!r})'.format(self.value)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.pickle_str = ''  # 序列化后的字符串

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

    def pre_order_traversal(self, current_node):
        '''树的遍历：深度优先，使用递归实现
        先序遍历: 根、左、右
        '''
        if current_node is None:  # 递归的终止条件
            self.pickle_str += '#!'
            return

        self.pickle_str = self.pickle_str + str(current_node.value) + '!'
        self.pre_order_traversal(current_node.left_child)  # 如果当前节点(叶子节点)没有左节点，则传入的是None，会终止递归
        self.pre_order_traversal(current_node.right_child)

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
        self.pre_order_traversal(self.root)
        print('按先序遍历序列化后的字符串: ', self.pickle_str)

        basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录
        with open(os.path.join(basepath, 'pickle_result.txt'), 'w') as f:
            f.write(self.pickle_str)


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

    # 序列化
    binary_tree.pickling()

    # 反序列化
    binary_tree.unpickling()
