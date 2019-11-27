from itertools import product

#A = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
#A = [0, 1, 2]


def check_ascending(sequence):
    for idx in range(1, len(sequence)):
        if sequence[idx] <= sequence[idx - 1]:
            return False
    return True


def solution(A):
    ascendings = {}
    pairs = [pair for pair in product(range(len(A)), range(len(A))) if pair[0] <= pair[1]]

    for pair in pairs:
        if pair[0] == pair[1]:
            ascendings.update({pair[0]: 1})
        else:
            sequence = A[pair[0]:(pair[1] + 1)]
            if check_ascending(sequence):
                ascendings.update({pair[0]: len(sequence)})
    else:
        max_value = max(ascendings.values())
        results = [elm[0] for elm in ascendings.items() if elm[1] == max_value]

    return results[0]