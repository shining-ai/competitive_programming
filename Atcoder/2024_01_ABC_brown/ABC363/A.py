import io
import sys


_INPUT = """\
123
"""


def debug_input():

    sys.stdin = io.StringIO(_INPUT)


def main():
    R = int(input())
    if R <= 99:
        print(100 - R)
    elif R <= 199:
        print(200 - R)
    elif R <= 299:
        print(300 - R)
    else:
        print(400 - R)


if __name__ == "__main__":
    # debug_input()
    main()
