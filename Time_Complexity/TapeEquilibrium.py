import sys


def solution(A):

    difference = sys.maxsize
    left = 0
    right = sum(A)

    for i in range(0, len(A)-1):
        left += A[i]
        right -= A[i]

        if abs(right - left) < difference:
            difference = abs(right - left)

    return difference


def test_solution():
    assert solution([3, 1, 2, 4, 3]) == 1
