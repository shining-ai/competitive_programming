import io
import sys
from collections import defaultdict
from bisect import bisect_left

_INPUT = """\
5
1 4 3 2 5
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    asc_nums = [0] * (N)  # 最長増加部分列問題を解く
    last_index = [0]
    for i in range(N):
        length = bisect_left(last_index, A[i])
        asc_nums[i] = length
        if len(last_index) <= length:
            last_index.append(A[i])
        else:
            last_index[length] = A[i]
    for i in range(1, N):  # iまでの部分列の最大値になるように修正
        asc_nums[i] = max(asc_nums[i - 1], asc_nums[i])

    desc_nums = [0] * (N)  # 最長減少部分列問題を解く
    last_index = [0]
    for i in range(N - 1, -1, -1):
        length = bisect_left(last_index, A[i])
        desc_nums[i] = length
        if len(last_index) <= length:
            last_index.append(A[i])
        else:
            last_index[length] = A[i]
    for i in range(N - 2, -1, -1):  # iまでの部分列の最大値になるように修正
        desc_nums[i] = max(desc_nums[i + 1], desc_nums[i])

    max_length = 0
    for i in range(N):
        max_length = max(max_length, asc_nums[i] + desc_nums[i] - 1)

    print(max_length)


if __name__ == "__main__":
    # debug_input()
    main()
