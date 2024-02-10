import io
import sys


def debug_input():
    _INPUT = """\
        5
1 20
1 30
2 1
1 40
2 3

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    Q = int(input())
    A = []

    for _ in range(Q):
        query, val = map(int, input().split())
        if query == 1:
            A.append(val)
        elif query == 2:
            print(A[-val])


if __name__ == "__main__":
    # debug_input()
    main()
