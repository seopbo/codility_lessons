from itertools import product, chain

A = [[2, 7, 5],
     [3, 1, 1],
     [2, 1, -7],
     [0, 2, 1],
     [1, 6, 8]]


def solution(A):
    N = len(A)
    M = len(A[0])

    points = product(range(N), range(M))
    equilibrium_points = []

    for point in points:
        if point[0] == 0:
            sum_above_row = 0
            sum_below_row = sum(chain.from_iterable(A[point[0] + 1:]))
        elif point[0] == N - 1:
            sum_above_row = sum(chain.from_iterable(A[:point[0]]))
            sum_below_row = 0
        else:
            sum_above_row = sum(chain.from_iterable(A[:point[0]]))
            sum_below_row = sum(chain.from_iterable(A[point[0] + 1:]))

        if point[1] == 0:
            sum_left_col = 0
            sum_right_col = sum(chain.from_iterable([[row[col] for row in A] for col in range(point[1] + 1, M)]))

        elif point[1] == M - 1:
            sum_left_col = sum(chain.from_iterable([[row[col] for row in A] for col in range(M)]))
            sum_right_col = 0
        else:
            sum_left_col = sum(chain.from_iterable([[row[col] for row in A] for col in range(point[1])]))
            sum_right_col = sum(chain.from_iterable([[row[col] for row in A] for col in range(point[1] + 1, M)]))

        if sum_above_row == sum_below_row and sum_left_col == sum_right_col:
            equilibrium_points.append(point)

    return len(equilibrium_points)
