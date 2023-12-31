import io
import sys


def debug_input():
    _INPUT = """\
30 30
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................
..............................

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(HW)
def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]

    dp[0][1] = 1

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if C[i - 1][j - 1] == ".":
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

    print(dp[H][W])


if __name__ == "__main__":
    # debug_input()
    main()
