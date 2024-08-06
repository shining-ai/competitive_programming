import io
import sys

_INPUT = """\
1
869
120
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    cost = 0
    for i in range(N):
        cost += abs(A[i] - B[i])
    print(cost)


if __name__ == "__main__":
    # debug_input()
    main()
