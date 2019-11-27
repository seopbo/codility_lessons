A = [100, 250, 1000]


def solution(A):

    merge_time = 0

    while len(A) > 1:
        min_time = A.pop(A.index(min(A)))
        merge_time += min_time

    merge_time = merge_time * 2 + A[0]
    return merge_time
