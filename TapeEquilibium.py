import sys


def solution(A):
    sum_left = 0
    sum_right = sum(A)
    min_diff = sys.maxsize

    for i in range(len(A)-1):
        sum_left += A[i]
        sum_right -= A[i]
        min_diff = min(min_diff, abs(sum_left - sum_right))

    return min_diff


def test_solution():
    assert solution([3, 1, 2, 4, 3]) == 1
