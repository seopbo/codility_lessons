def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    return P


def count_total(P, x, y):
    return P[y + 1] - P[x]
