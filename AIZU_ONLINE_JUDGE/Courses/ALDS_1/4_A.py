import io
import sys


def debug_input():
    _INPUT = """\
5
1 2 3 4 5
3
3 4 1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = set(map(int, input().split()))
    q = int(input())
    T = set(map(int, input().split()))
    print(len(S & T))


if __name__ == "__main__":
    # debug_input()
    main()
