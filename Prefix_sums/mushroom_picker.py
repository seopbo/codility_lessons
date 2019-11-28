def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def suffix_sums(A):
    n = len(A)
    S = [0] * (n + 1)

    for i in range(n - 1, -1, - 1):
        S[i] = A[i] + S[i+1]
    return S


def count_total(P, x, y):
    return P[y + 1] - P[x]

# k spot
# m number of steps
def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    for p in range(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))

    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result


A = [2, 3, 7, 5, 1, 3, 9]
k, m = 4, 6

mushrooms(A, k, m)
