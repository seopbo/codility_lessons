def enumerate_fibonacci_number(n):
    a = 0
    b = 1

    while a <= n:
        print(a)
        c = a + b
        a = b
        b = c

enumerate_fibonacci_number(10)