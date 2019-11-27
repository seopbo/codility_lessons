import re
import math
from collections import defaultdict


T = ['test1a', 'test2', 'test1b', 'test1c',
     'test3']
R = ['Wrong answer', 'OK', 'Runtime error',
     'OK', 'Time limit exceeded']


def solution(T, R):
    group = defaultdict(list)
    length = len(T)

    for idx in range(length):
        group[re.findall('\\d+', T[idx])[0]].append(R[idx])
    else:
        results = [all([test == 'OK' for test in v]) for _, v in group.items()]

    score = math.floor(sum(results) / len(results) * 100)
    return score
