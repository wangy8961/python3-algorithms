def binary_search(L, item):
    '''递归实现二分查找，输入的列表必须是有序的（比如，从小到大排列）'''
    if len(L) == 0:
        return False
    else:
        midpoint = len(L) // 2
        print('midpoint = {}'.format(midpoint))  # 测试
        if L[midpoint] == item:  # 找到了
            return True
        else:
            if item < L[midpoint]:  # 说明 item 在左半部分
                return binary_search(L[:midpoint], item)
            else:  # 说明 item 在右半部分
                return binary_search(L[midpoint+1:], item)


if __name__ == '__main__':
    L1 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    item = 31
    # item = 32  # 测试
    print('{} 是否在列表中: {}'.format(item, binary_search(L1, item)))
