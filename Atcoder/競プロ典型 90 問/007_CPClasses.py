import io
import sys
import bisect

_INPUT = """\
4
4000 4400 5000 3200
3
3312
2992
4229
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    A.sort()

    for q in range(Q):
        b = int(input())
        i = bisect.bisect_left(A, b)
        if i == 0:
            print(abs(A[i] - b))
        elif i == N:
            print(abs(A[i - 1] - b))
        else:
            print(min(abs(A[i - 1] - b), abs(A[i] - b)))


if __name__ == "__main__":
    # debug_input()
    main()
