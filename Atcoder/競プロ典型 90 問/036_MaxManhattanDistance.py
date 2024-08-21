import io
import sys

_INPUT = """\
3 3
-1 2
1 1
-2 -3
1
2
3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P_rotated_45 = [[p[0] + p[1], p[1] - p[0]] for p in P]
    x_min = min(P_rotated_45, key=lambda x: x[0])[0]
    x_max = max(P_rotated_45, key=lambda x: x[0])[0]
    y_min = min(P_rotated_45, key=lambda x: x[1])[1]
    y_max = max(P_rotated_45, key=lambda x: x[1])[1]
    for _ in range(Q):
        q = int(input()) - 1
        x, y = P_rotated_45[q]
        max_distance = max(
            abs(x - x_min),
            abs(x - x_max),
            abs(y - y_min),
            abs(y - y_max),
        )
        print(max_distance)


if __name__ == "__main__":
    # debug_input()
    main()
