import io
import sys


def debug_input():
    _INPUT = """\
7
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    for i in range(N):
        if i % 3 == 2:
            print("x", end="")
        else:
            print("o", end="")


if __name__ == "__main__":
    # debug_input()
    main()
