import io
import sys


def debug_input():
    _INPUT = """\
6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#...

    """

    sys.stdin = io.StringIO(_INPUT)


def count_hash(board, w, h):
    count = 0

    if board[w - 1][h - 1] == "#":
        count += 1
    if board[w - 1][h] == "#":
        count += 1
    if board[w - 1][h + 1] == "#":
        count += 1
    if board[w][h - 1] == "#":
        count += 1
    if board[w][h + 1] == "#":
        count += 1
    if board[w + 1][h - 1] == "#":
        count += 1
    if board[w + 1][h] == "#":
        count += 1
    if board[w + 1][h + 1] == "#":
        count += 1

    return count


# 計算量: O(N!)
def main():
    H, W = map(int, input().split())

    board = [["." for _ in range(W + 2)] for _ in range(H + 2)]
    ans = [["." for _ in range(W)] for _ in range(H)]
    for i in range(1, H + 1):
        S = input()
        for j in range(1, W + 1):
            board[i][j] = S[j - 1]

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if board[i][j] == ".":
                ans[i - 1][j - 1] = str(count_hash(board, i, j))
            else:
                ans[i - 1][j - 1] = "#"

    print("\n".join(["".join(ans[i]) for i in range(H)]))


if __name__ == "__main__":
    # debug_input()
    main()
