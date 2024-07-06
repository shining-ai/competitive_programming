import io
import sys

_INPUT = """\
8 8 3
9 9 8 2 4 4 3 5

"""


def debug_input():

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    B = A[:K]
    B.append(X)
    B += A[K:]
    print(" ".join(map(str, B)))


if __name__ == "__main__":
    # debug_input()
    main()
