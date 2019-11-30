A = [1,1,0,0]


def grocery_store(A):
    n = len(A)
    size, result = 0, 0

    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size)
    return result


grocery_store(A)