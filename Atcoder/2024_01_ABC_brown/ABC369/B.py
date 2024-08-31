import io
import sys

_INPUT = """\
4
3 L
6 R
9 L
1 R
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    tiredness = 0
    left = float("inf")
    right = float("inf")
    for _ in range(N):
        A, S = input().split()
        A = int(A)
        if S == "L":
            if left == float("inf"):
                left = A
                continue
            tiredness += abs(A - left)
            left = A
        else:
            if right == float("inf"):
                right = A
                continue
            tiredness += abs(A - right)
            right = A
    print(tiredness)


if __name__ == "__main__":
    # debug_input()
    main()
