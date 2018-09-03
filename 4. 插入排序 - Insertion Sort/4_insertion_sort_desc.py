from timeit import timeit


def insertion_sort(L):
    '''插入排序，降序'''
    n = len(L)
    if n == 1:
        return

    for i in range(1, n):
        temp = L[i]
        j = i - 1
        while j >= 0 and temp > L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = temp


if __name__ == '__main__':
    L1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    L2 = L1.copy()

    print('Before: ', L1)
    insertion_sort(L1)
    print('After: ', L1)

    print('Insertion sort function run 1,000,000 times, cost: ', timeit('insertion_sort(L2)', 'from __main__ import insertion_sort, L2'), 'seconds.')


# Output:
# Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
# After:  [93, 77, 55, 54, 44, 31, 26, 20, 17]
# Insertion sort function run 1,000,000 times, cost:  5.185071438 seconds.
