import io
import sys


def debug_input():
    _INPUT = """\
    6
    9 1 4 4 6 7
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    d = list(map(int, input().split()))

    d.sort()
    center = len(d) // 2
    if d[center] == d[center - 1]:
        print(0)
    else:
        print(d[center] - d[center - 1])


if __name__ == "__main__":
    # debug_input()
    main()
