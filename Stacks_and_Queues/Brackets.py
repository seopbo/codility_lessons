def solution(S):

    if len(S) % 2 != 0:
        return 0

    if len(S) == 0:
        return 1

    stack = []

    for bracket in S:

        if not stack:
            stack.append(bracket)
            continue

        if stack[-1] == '{' and bracket == '}':
            stack.pop()
        elif stack[-1] == '[' and bracket == ']':
            stack.pop()
        elif stack[-1] == '(' and bracket == ')':
            stack.pop()
        else:
            stack.append(bracket)

    if not stack:
        return 1
    else:
        return 0


def test_solution():
    assert solution('{[()()]}') == 1
    assert solution('({)()]') == 0


