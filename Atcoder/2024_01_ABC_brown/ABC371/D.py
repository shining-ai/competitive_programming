import io
import sys
from bisect import bisect_left, bisect_right

_INPUT = """\
4
1 3 5 7
1 2 3 4
4
1 1
2 6
0 10
2 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    X = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ruisekiwa = [0] * (N + 1)
    for i in range(N):
        ruisekiwa[i + 1] = ruisekiwa[i] + P[i]
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        left = bisect_left(X, L)
        right = bisect_right(X, R)
        print(ruisekiwa[right] - ruisekiwa[left])


if __name__ == "__main__":
    # debug_input()
    main()
