import io
import sys

_INPUT = """\
2023
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    Y = int(input())
    if Y % 400 == 0:
        print(366)
        return
    if Y % 100 == 0:
        print(365)
        return
    if Y % 4 == 0:
        print(366)
        return
    print(365)


if __name__ == "__main__":
    # debug_input()
    main()
