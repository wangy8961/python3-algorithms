def sequential_search(L, item):
    '''顺序查找，输入的列表是有序的（比如，从小到大排列）'''
    pos = 0
    found = False  # 标记是否已找到数据项
    stop = False  # 如果遍历到的元素值比 item 大，则说明不用再继续了（因为后续的元素肯定都比 item 大）

    while pos < len(L) and not found and not stop:
        # print(pos)  # 测试
        if L[pos] == item:  # 表示找到了
            found = True
        else:
            if L[pos] > item:
                stop = True
            else:
                pos += 1

    return found


if __name__ == '__main__':
    L1 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    item = 31
    # item = 32  # 测试
    print('{} 是否在列表中: {}'.format(item, sequential_search(L1, item)))
