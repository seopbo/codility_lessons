def solution(N, A):
    counters = [0] * N
    start_line = 0
    current_max = 0

    for X in A:
        if X > N:
            start_line = current_max
        elif counters[X-1] < start_line:
            counters[X-1] = start_line + 1
        else:
            counters[X-1] += 1

        if X <= N and counters[X-1] > current_max:
            current_max = counters[X-1]

    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line

    return counters


def test_solution():
    assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
