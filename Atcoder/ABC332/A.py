import io
import sys


def debug_input():
    _INPUT = """\
3 2000 500
1000 1
100 6
5000 1

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, S, K = map(int, input().split())
    ans = 0

    for i in range(N):
        P, Q = map(int, input().split())
        ans += P * Q

    if ans < S:
        ans += K

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
