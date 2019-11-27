string_1 = 'ACCAABBC'
string_2 = 'ABCBBCBA'
string_3 = 'BABABA'


def solution(S):
    stack = []

    for char in S:
        print(char)
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


