from collections import Counter


def solution(N):
    count = Counter(N)
    for key in count:
        if count.get(key) % 2 != 0:
            return key


def test_solution():
    assert solution([9, 3, 9, 3, 9, 7, 9])
