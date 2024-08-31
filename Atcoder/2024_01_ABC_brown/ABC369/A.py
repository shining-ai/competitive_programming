import io
import sys

_INPUT = """\
5 7
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B = map(int, input().split())
    if A == B:
        print(1)
        return
    if (A + B) % 2 == 0:
        print(3)
    else:
        print(2)


if __name__ == "__main__":
    # debug_input()
    main()
