import io
import sys

_INPUT = """\
5 5
1 2
1 3
3 2
5 2
4 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    smaller_point_nums = [set() for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        smaller_point_nums[max(a, b) - 1].add(min(a, b) - 1)

    count = 0
    for i in range(N):
        if len(smaller_point_nums[i]) != 1:
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
