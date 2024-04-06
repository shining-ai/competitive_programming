import collections
import io
import sys


def debug_input():
    _INPUT = """\
10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    color_min_taste = collections.defaultdict(lambda: float("inf"))
    for i in range(N):
        taste, color = map(int, input().split())
        color_min_taste[color] = min(color_min_taste[color], taste)
    print(max(color_min_taste.values()))


if __name__ == "__main__":
    # debug_input()
    main()
