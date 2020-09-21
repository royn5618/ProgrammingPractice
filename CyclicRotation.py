# Challenge Link - https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# My Results - https://app.codility.com/demo/results/trainingFGAZZW-5XB/

def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return []
    idx = [i for i in range(0, len(A))]
    while K:
        idx = [i + 1 for i in idx]
        max_index = idx.index(max(idx))
        idx[max_index] = 0
        K = K - 1
    new_list = [0] * len(A)
    for n, index in zip(A, idx):
        new_list[index] = n
    return new_list
