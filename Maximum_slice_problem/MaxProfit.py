from sys import maxsize


def solution(A):
    P = []

    for i in range(1, len(A)):
        P.append(A[i] - A[i-1])

    max_ending = 0
    max_profit = -maxsize

    for p in P:
        max_ending += p

        if max_profit < max_ending:
            max_profit = max_ending

        if max_ending < 0:
            max_ending = 0

    return max_profit if max_profit > 0 else 0


def test_solution():
    assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
