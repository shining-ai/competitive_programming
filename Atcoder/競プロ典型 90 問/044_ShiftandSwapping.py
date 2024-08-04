import io
import sys

_INPUT = """\
8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    shift_right = 0
    for _ in range(Q):
        T, X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        X = (-shift_right + X) % N
        Y = (-shift_right + Y) % N
        if T == 1:
            A[X], A[Y] = A[Y], A[X]
        elif T == 2:
            shift_right += 1
        else:
            print(A[X])


if __name__ == "__main__":
    # debug_input()
    main()
