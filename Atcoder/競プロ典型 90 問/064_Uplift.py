import io
import sys

_INPUT = """\
3 3
1 2 3
2 3 1
1 2 -1
1 3 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    height_differences = []
    for i in range(1, N):
        height_differences.append(A[i] - A[i - 1])
    inconvinience = sum([abs(diff) for diff in height_differences])
    for i in range(Q):
        L, R, V = map(int, input().split())
        L -= 1
        R -= 1
        if L != 0:
            prev = height_differences[L - 1]
            height_differences[L - 1] += V
            changed = abs(height_differences[L - 1]) - abs(prev)
            inconvinience += changed
        if R < N - 1:
            prev = height_differences[R]
            height_differences[R] -= V
            changed = abs(height_differences[R]) - abs(prev)
            inconvinience += changed
        print(inconvinience)


if __name__ == "__main__":
    # debug_input()
    main()
