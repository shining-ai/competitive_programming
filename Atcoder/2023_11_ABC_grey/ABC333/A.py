import io
import sys


def debug_input():
    _INPUT = """\
    3

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())

    print(str(N) * N)


if __name__ == "__main__":
    # debug_input()
    main()
