import io
import sys


def debug_input():
    _INPUT = """\
    4
    10 2
    10 1
    10 2
    3 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    takahashi = 0
    aoki = 0

    for i in range(N):
        X, Y = map(int, input().split())
        takahashi += X
        aoki += Y

    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    # debug_input()
    main()
