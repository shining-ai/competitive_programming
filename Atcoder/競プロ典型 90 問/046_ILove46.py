import io
import sys
from collections import defaultdict

_INPUT = """\
3
10 13 93
5 27 35
55 28 52
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A_count = defaultdict(int)
    B_count = defaultdict(int)
    C_count = defaultdict(int)

    for i in range(N):
        A_count[A[i] % 46] += 1
        B_count[B[i] % 46] += 1
        C_count[C[i] % 46] += 1

    combination_46 = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 != 0:
                    continue
                combination_46 += A_count[i] * B_count[j] * C_count[k]
    print(combination_46)


if __name__ == "__main__":
    # debug_input()
    main()
