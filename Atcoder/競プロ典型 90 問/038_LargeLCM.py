import io
import sys
import math

_INPUT = """\
4 6
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def Euclidean(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def main():
    A, B = map(int, input().split())
    # gcd = math.gcd(A, B)
    gcd = Euclidean(A, B)
    if 10**18 < A * B // gcd:
        print("Large")
        return
    print(A * B // gcd)


if __name__ == "__main__":
    # debug_input()
    main()
