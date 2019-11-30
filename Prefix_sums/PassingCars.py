def solution(A):

    if sum(A) == len(A) or sum(A) == 0:
        return 0

    n = len(A)
    P = [0] * (n + 1)

    car = [idx for idx, car in enumerate(A) if car == 0]

    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]

    passing_cars = [P[-1] - P[car+1] for car in car]
    passing_cars = sum(passing_cars)

    if passing_cars > int(1e+9):
        return -1

    return passing_cars


def test_solution():
    assert solution([0, 1, 0, 1, 1]) == 5
