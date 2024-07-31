import io
import sys


def debug_input():
    _INPUT = """\
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sum_A = sum(A)
    sum_B = sum(B)

    if sum_B - sum_A > 0:
        print(0)
    else:
        print(abs(sum_B - sum_A) + 1)


if __name__ == "__main__":
    # debug_input()
    main()
