import io
import math
import sys


def debug_input():
    _INPUT = """\
-20
-13
27
123456789123456789
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    X = int(input())
    quotient = X // 10
    if X % 10 == 0:
        print(quotient)
    else:
        print(quotient + 1)


if __name__ == "__main__":
    # debug_input()
    main()
