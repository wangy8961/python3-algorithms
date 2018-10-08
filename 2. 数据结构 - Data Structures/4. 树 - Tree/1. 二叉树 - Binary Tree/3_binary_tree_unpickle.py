import os
from binary_tree import BinaryTree

def unpickling(filename):
    
    with open(filename, 'r') as f:
        result = f.read()
        print(result)

    # ['0', '1', '3', '7', '#', '#', '8', '#', '#', '4', '9', '#', '#', '#', '2', '5', '#', '#', '6', '#', '#', '']
    values = result.split('!')
    # 移除最后一个元素：''  注意不能 remove('')，因为可能添加节点时，就是添加binary_tree.breadth_first_add('')
    del values[-1]
    print(values)

    binary_tree = BinaryTree()  # 创建空树
    for value in values:
        if binary_tree.root is None:
            binary_tree.breadth_first_add(value)  # 添加根节点
        else:


if __name__ == '__main__':
    basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录
    filename = os.path.join(basepath, 'pickle_result.txt')