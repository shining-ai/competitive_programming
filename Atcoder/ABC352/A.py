import io
import sys


def debug_input():
    _INPUT = """\
100 23 67 45


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, X, Y, Z = map(int, input().split())
    if X <= Z <= Y:
        print("Yes")
    elif Y <= Z <= X:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
