def binary_search(L, item):
    '''非递归实现二分查找，输入的列表必须是有序的（比如，从小到大排列）'''
    first = 0
    last = len(L) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        print('first = {}, last = {}, midpoint = {}'.format(first, last, midpoint))  # 测试
        if L[midpoint] == item:  # 找到了
            found = True
        else:
            if item < L[midpoint]:  # 说明 item 在左半部分
                last = midpoint - 1
            else:  # 说明 item 在右半部分
                first = midpoint + 1

    return found


if __name__ == '__main__':
    L1 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    item = 31
    # item = 32  # 测试
    print('{} 是否在列表中: {}'.format(item, binary_search(L1, item)))
