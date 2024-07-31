import io
import sys
import bisect
import math


def debug_input():
    _INPUT = """\
5
1 3 99999999 99999994 1000000


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    num_over = 0
    A.sort()
    all_sum = sum(A) * (N - 1)

    # 二分探索を使うとO(logN)なのになぜかTLEになる
    # index = N
    # for i in range(N - 1, -1, -1):
    #     index = bisect.bisect_left(A[i + 1 : index + 1], 10**8 - A[i]) + i + 1
    #     num_over += N - index

    right = N - 1
    for i in range(N - 1):
        right = max(right, i + 1)
        while i < right and A[right] >= 10**8 - A[i]:
            right -= 1
        num_over += N - right - 1
    print(all_sum - num_over * 10**8)


if __name__ == "__main__":
    # debug_input()
    main()
