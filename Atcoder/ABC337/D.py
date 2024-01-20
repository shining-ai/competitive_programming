import io
import sys


def debug_input():
    _INPUT = """\
4 2 3
.o
.o
.o
.o

    """

    sys.stdin = io.StringIO(_INPUT)


def brute_force():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    # dp = [[10**6] * W for _ in range(H)]
    ans = 10**6

    for i_h in range(H):
        for i_w in range(W - K + 1):
            if S[i_h][i_w] == "o" or S[i_h][i_w] == ".":
                cnt = 0
                for j in range(K):
                    if S[i_h][i_w + j] == ".":
                        cnt += 1
                    elif S[i_h][i_w + j] == "x":
                        break
                else:
                    # dp[i_h][i_w] = cnt
                    ans = min(ans, cnt)

    for i_w in range(W):
        for i_h in range(H - K + 1):
            if S[i_h][i_w] == "o" or S[i_h][i_w] == ".":
                cnt = 0
                for j in range(K):
                    if S[i_h + j][i_w] == ".":
                        cnt += 1
                    elif S[i_h + j][i_w] == "x":
                        break
                else:
                    # dp[i_h][i_w] = min(dp[i_h][i_w], cnt)
                    ans = min(ans, cnt)

    # print(dp)
    if ans == 10**6:
        print(-1)
    else:
        print(ans)


def main():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 10**6

    w_cnt = [[0] * W for _ in range(H)]
    h_cnt = [[0] * W for _ in range(H)]

    for i_h in range(H):
        for i_w in range(1,W):
            if S[i_h][i_w] == "o" or S[i_h][i_w] == ".":
                w_cnt[i_h][i_w] = w_cnt[i_h][i_w - 1] + 1

    for i_w in range(W):
        for i_h in range(1,H):
            if S[i_h][i_w] == "o" or S[i_h][i_w] == ".":
                h_cnt[i_h][i_w] = h_cnt[i_h - 1][i_w] + 1


    print(w_cnt)


if __name__ == "__main__":
    debug_input()
    main()
