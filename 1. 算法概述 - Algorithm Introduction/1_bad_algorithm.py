from timethis import timethis


@timethis
def combination():  # 算法1，3层for循环，时间复杂度为O(n^3)
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    print("a, b, c: %d, %d, %d" % (a, b, c))


if __name__ == '__main__':
    combination()

# Output:
# a, b, c: 0, 500, 500
# a, b, c: 200, 375, 425
# a, b, c: 375, 200, 425
# a, b, c: 500, 0, 500
# Function combination() in model __main__ cost: 1137.25 seconds
