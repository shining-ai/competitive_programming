import io
import sys

_INPUT = """\
5
3 1 5 4 6
"""

#    偶     奇
# 1   0      1
# 2   5      2
# 3   12     10
# 4   18     13 # 前の奇数のを使う
# 5   27     25


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_point = [[0] * 2 for _ in range(N)]  # 0: 偶数倒した, 1: 奇数倒した
    max_point[0][0] = 0
    max_point[0][1] = A[0]
    for i, a in enumerate(A[1:], start=1):
        max_point[i][0] = max(max_point[i - 1][1] + a * 2, max_point[i - 1][0])
        max_point[i][1] = max(max_point[i - 1][0] + a, max_point[i - 1][1])
    print(max(max_point[-1]))


if __name__ == "__main__":
    # debug_input()
    main()
