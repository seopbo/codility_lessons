from bisect import bisect

S = 'banana'


def solution(S):
    unicodes = [ord(char) for char in S]

    sequence = []
    for unicode in unicodes:
        idx = bisect(sequence, unicode)
        if idx == len(sequence):
            sequence.append(unicode)
        else:
            sequence[idx] = unicode

    return len(unicodes) - len(sequence)
