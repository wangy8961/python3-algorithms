from timethis import timethis


@timethis
def combination():  # 算法2，2层for循环，时间复杂度为O(n^2)
    for a in range(1001):
        for b in range(1001-a):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print("a, b, c: %d, %d, %d" % (a, b, c))


if __name__ == '__main__':
    combination()

# Output:
# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# Function combination() in model __main__ cost: 0.65625 seconds
