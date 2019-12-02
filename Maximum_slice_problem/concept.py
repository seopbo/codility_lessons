from sys import maxsize


def golden_max_slice(a): # kadane algorithm
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(len(a)):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

