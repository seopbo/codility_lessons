from collections import Counter


def solution(A):
    counter = Counter(A)
    for key in counter.keys():
        if counter.get(key) % 2 != 0:
            return key


def test_solution():
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
