import io
import sys


_INPUT = """\
8 3
31 43 26 6 18 36 22 13
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    min_difference = float("inf")

    A.sort()
    left = 0
    right = N - K - 1
    while right < N:
        min_difference = min(min_difference, A[right] - A[left])
        left += 1
        right += 1

    print(min_difference)


if __name__ == "__main__":
    # debug_input()
    main()
