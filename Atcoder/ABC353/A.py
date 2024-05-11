import io
import sys


def debug_input():
    _INPUT = """\
7
10 5 10 2 10 13 15

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    H = list(map(int, input().split()))

    base = H[0]
    for i, h in enumerate(H[1:]):
        if h > base:
            print(i+2)
            return
    print(-1)


if __name__ == "__main__":
    # debug_input()
    main()
