import io
import sys


def debug_input():
    _INPUT = """\
        3 9 2

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B, D = map(int, input().split())

    for i in range(A, B + 1, D):
        print(i)


if __name__ == "__main__":
    # debug_input()
    main()
