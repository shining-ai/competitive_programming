import io
import sys

_INPUT = """\
5 3
1 2 3 4 5
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = A[-K:] + A[:-K]
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    # debug_input()
    main()
