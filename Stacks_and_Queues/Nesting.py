def solution(S):

    if len(S) == 0:
        return 1

    if len(S) % 2 != 0:
        return 0

    stack = []

    for bracket in S:
        if bracket == '(':
            stack.append(bracket)
        else:
            if stack:
                stack.pop()
            else:
                return 0

    return 0 if stack else 1


def test_solution():
    assert solution("(()(())())") == 1