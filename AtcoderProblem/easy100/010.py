import io
import sys


def debug_input():
    _INPUT = """\
4
20 18 2 18

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    sum_a = 0
    sum_b = 0

    for i, a in enumerate(A):
        if i % 2 == 0:
            sum_a += a
        else:
            sum_b += a

    print(sum_a - sum_b)


if __name__ == "__main__":
    # debug_input()
    main()
