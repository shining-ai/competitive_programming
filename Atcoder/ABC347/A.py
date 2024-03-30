import io
import sys


def debug_input():
    _INPUT = """\
5 2
2 5 6 7 10
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for a in A:
        if a % K != 0:
            continue
        print(a // K, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
