import io
import sys

_INPUT = """\
7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    cumulative = [(0, 0)]
    for _ in range(N):
        c, p = map(int, input().split())
        if c == 1:
            prev_score = cumulative[-1]
            cumulative.append((prev_score[0] + p, prev_score[1]))
        else:
            prev_score = cumulative[-1]
            cumulative.append((prev_score[0], prev_score[1] + p))

    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        print(cumulative[r][0] - cumulative[l-1][0], cumulative[r][1] - cumulative[l-1][1])


if __name__ == "__main__":
    # debug_input()
    main()
