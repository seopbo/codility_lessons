def solution(H):
    stack = []
    count = 0

    for h in H:

        while len(stack) > 0 and stack[len(stack) - 1] > h:
            stack.pop()

        if len(stack) == 0 or stack[len(stack) - 1] < h:
            stack.append(h)
            count += 1

    return count


def test_solution():
    assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7