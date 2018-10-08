def insertion_sort(L):
    '''插入排序，降序'''
    n = len(L)
    if n <= 1:
        return

    for i in range(1, n):
        temp = L[i]
        j = i
        while j >= 1 and temp > L[j-1]:
            L[j] = L[j-1]
            j -= 1
        L[j] = temp


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
