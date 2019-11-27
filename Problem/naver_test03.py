from bisect import bisect

S = 'banana'


def solution(S):
    list_of_codept = [ord(char) for char in S]

    sequence = []

    for codept in list_of_codept:
        idx = bisect(sequence, codept)
        if idx == len(sequence):
            sequence.append(codept)
        else:
            sequence[idx] == codept

    return len(list_of_codept) - len(sequence)