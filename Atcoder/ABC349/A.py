import io
import sys


def debug_input():
    _INPUT = """\
6
10 20 30 40 50

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    print(-sum_A)



if __name__ == "__main__":
    # debug_input()
    main()
