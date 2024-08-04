import io
import sys
import math

_INPUT = """\
4 3 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    a, b, c = map(int, input().split())
    if a < c ** b:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
