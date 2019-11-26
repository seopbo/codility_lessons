def print_triangle(n):
    for row in range(1, n + 1):
        for _ in range(row):
            print('*', end=' ')
        print()

print_triangle(4)