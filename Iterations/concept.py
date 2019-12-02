def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))


def print_triangle(n):
    for row in range(1, n + 1):
        for _ in range(row):
            print('*', end=' ')
        print()


print_triangle(4)


def print_symmetric_triangle(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end=' ')
        for j in range(2 * i - 1):
            print('*', end=' ')
        print()


print_symmetric_triangle(4)


def count_digits(n):
    result = 0

    while n > 0:
        n = n // 10
        result += 1

    return result


print(count_digits(20))


def enumerate_fibonacci_number(n):
    a = 0
    b = 1

    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c
