import io
import sys


def debug_input():
    _INPUT = """\
4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    print(1, end="")
    for _ in range(N):
        print(0, end="")
        print(1, end="")
    print()


if __name__ == "__main__":
    # debug_input()
    main()
