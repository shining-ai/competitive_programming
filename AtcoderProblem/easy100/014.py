import io
import sys


def debug_input():
    _INPUT = """\
7 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())

    ans = N % K
    ans = min(ans, abs(ans - K))

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
