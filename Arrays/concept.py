def reverse(A):
    for i in range(len(A) // 2):
        A[i], A[len(A) - i - 1] = A[len(A) - i - 1], A[i]


A = [1, 2, 3, 4, 5, 6, 7]
reverse(A)
print(A)