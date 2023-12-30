import bisect
import io
import sys


def debug_input():
    _INPUT = """\
5 65 7 37
5 15 30 50 55
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, W, L, R = map(int, input().split())
    X = [0] + list(map(int, input().split())) + [W]
    MOD = 10**9 + 7  # = 1000000007

    dp = [0] * (N + 2)
    dp_sum = [0] * (N + 2)

    for i in range(1, N + 2):
        posL = max(bisect.bisect_left(X, X[i] - R) - 1, 0)
        posR = bisect.bisect_right(X, max(X[i] - L, 0)) - 1

        if L <= X[i] <= R:
            dp[i] += 1

        dp[i] += dp_sum[posR] - dp_sum[posL]
        dp_sum[i] = dp_sum[i - 1] + dp[i]

    print(dp[-1] % MOD)


if __name__ == "__main__":
    # debug_input()
    main()
