import io
import sys

_INPUT = """\
2 2 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    A, B, C = map(int, input().split())

    def gcd(a, b):
        while a and b:
            if a >= b:
                a %= b
            else:
                b %= a
        return a + b

    size = gcd(A, gcd(B, C))
    print((A // size - 1) + (B // size - 1) + (C // size - 1))


if __name__ == "__main__":
    # debug_input()
    main()
