A = [0, 0, 4, 2, 4, 5]


def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)

    for k in range(n):
        count[A[k]] += 1
    return count


print(counting(A, 5))