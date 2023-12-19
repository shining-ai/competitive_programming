import io
import sys


def debug_input():
    _INPUT = """\
100
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())

    ans = 1
    while ans * 2 <= N:
        ans *= 2

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
