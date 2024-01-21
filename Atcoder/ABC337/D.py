import io
import sys


def debug_input():
    _INPUT = """\
3 4 3
xo.x
..o.
xx.o

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    d_cum_width = [[0] * (W + 1) for _ in range(H)]
    x_cum_width = [[0] * (W + 1) for _ in range(H)]

    d_cum_height = [[0] * W for _ in range(H + 1)]
    x_cum_height = [[0] * W for _ in range(H + 1)]

    for i_h in range(H):
        for i_w in range(W):
            d_cum_width[i_h][i_w + 1] = d_cum_width[i_h][i_w]
            x_cum_width[i_h][i_w + 1] = x_cum_width[i_h][i_w]
            if S[i_h][i_w] == ".":
                d_cum_width[i_h][i_w + 1] += 1
            elif S[i_h][i_w] == "x":
                x_cum_width[i_h][i_w + 1] += 1

    for i_w in range(W):
        for i_h in range(H):
            d_cum_height[i_h + 1][i_w] = d_cum_height[i_h][i_w]
            x_cum_height[i_h + 1][i_w] = x_cum_height[i_h][i_w]
            if S[i_h][i_w] == ".":
                d_cum_height[i_h + 1][i_w] += 1
            elif S[i_h][i_w] == "x":
                x_cum_height[i_h + 1][i_w] += 1

    ans = 10**6

    # print("d_cum_width")
    # for i in d_cum_width:
    #     print(i)
    # print("d_cum_height")
    # for i in d_cum_height:
    #     print(i)

    # print("x_cum_width")
    # for i in x_cum_width:
    #     print(i)
    # print("x_cum_height")
    # for i in x_cum_height:
    #     print(i)

    for i_h in range(H):
        for i_w in range(1, W - K + 2):
            if x_cum_width[i_h][i_w + K - 1] - x_cum_width[i_h][i_w - 1] == 0:
                ans = min(
                    ans,
                    d_cum_width[i_h][i_w + K - 1] - d_cum_width[i_h][i_w - 1],
                )

    for i_w in range(W):
        for i_h in range(1, H - K + 2):
            if (
                x_cum_height[i_h + K - 1][i_w] - x_cum_height[i_h - 1][i_w]
                == 0
            ):
                ans = min(
                    ans,
                    d_cum_height[i_h + K - 1][i_w]
                    - d_cum_height[i_h - 1][i_w],
                )

    if ans == 10**6:
        print(-1)
    else:
        print(ans)


def brute_force():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]
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
                    ans = min(ans, cnt)

    if ans == 10**6:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
