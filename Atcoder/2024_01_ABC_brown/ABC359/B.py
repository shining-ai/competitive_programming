import io
import sys


def debug_input():
    _INPUT = """\
4
4 3 2 3 2 1 4 1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    prev = None
    prev_2 = None
    ans = 0
    for a in A:
        if a == prev_2:
            ans += 1
        prev_2 = prev
        prev = a
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
