import io
import math
import sys


def debug_input():
    _INPUT = """\
2
10
1 100
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()
    C = list(map(int, input().split()))

    if N == 2:
        if S == "01" or S == "10":
            print(min(C[0], C[1]))
        else:
            print(0)
        return

    cost_01 = [0] * (N + 1)
    cost_10 = [0] * (N + 1)

    for i in range(N):
        if i % 2 == 0:
            if S[i] == "1":
                cost_01[i + 1] = cost_01[i] + C[i]
                cost_10[i + 1] = cost_10[i]
            else:
                cost_01[i + 1] = cost_01[i]
                cost_10[i + 1] = cost_10[i] + C[i]
        else:
            if S[i] == "1":
                cost_01[i + 1] = cost_01[i]
                cost_10[i + 1] = cost_10[i] + C[i]
            else:
                cost_01[i + 1] = cost_01[i] + C[i]
                cost_10[i + 1] = cost_10[i]

    ans = math.inf
    for idx in range(1, N - 1):
        cost_0110 = cost_01[idx] + cost_10[-1] - cost_10[idx + 1]
        cost_1001 = cost_10[idx] + cost_01[-1] - cost_01[idx + 1]
        ans = min(ans, cost_0110, cost_1001)
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
