def sequential_search(L, item):
    '''顺序查找，输入的列表是无序的'''
    pos = 0
    found = False  # 标记是否已找到数据项

    while pos < len(L) and not found:
        if L[pos] == item:  # 表示找到了
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    item = 31
    # item = 100  # 测试
    print('{} 是否在列表中: {}'.format(item, sequential_search(L1, item)))
