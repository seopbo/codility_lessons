from bisect import bisect, bisect_right, bisect_left

S = 'banana'
unicodes = [ord(char) for char in S]
[98, 97, 110, 97, 110, 97]
def solution(S):
    unicodes = [ord(char) for char in S]

    sequence = []
    for unicode in unicodes:
        idx = bisect_right(sequence, unicode)
        if idx == len(sequence):
            sequence.append(unicode)
        else:
            sequence[idx] = unicode

    return sequence


sequence = []
unicode = 97
idx = bisect(sequence, unicode)
solution(S)
bisect?
len(sequence)

bisect_left(unicodes, 120)