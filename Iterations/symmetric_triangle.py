def symmetric_triangle(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end=' ')
        for j in range(2 * i - 1):
            print('*', end=' ')
        print()

symmetric_triangle(4)