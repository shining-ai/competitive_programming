import io
import sys


def debug_input():
    _INPUT = """\
3
3 4 6
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    prev = A[0]
    ans = []
    for a in A[1:]:
        print(a*prev, end=" ")
        prev = a
    print()


if __name__ == "__main__":
    # debug_input()
    main()
