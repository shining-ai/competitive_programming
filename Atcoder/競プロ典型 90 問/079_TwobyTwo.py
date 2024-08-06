import io
import sys

_INPUT = """\
3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]
    change_num = 0

    def plus(h, w, num):
        A[h][w] += num
        A[h + 1][w] += num
        A[h][w + 1] += num
        A[h + 1][w + 1] += num

    for row in range(H - 1):
        for col in range(W - 1):
            num = B[row][col] - A[row][col]
            plus(row, col, num)
            change_num += abs(num)
        if A[row][W - 1] != B[row][W - 1]:
            print("No")
            return
    for col in range(W):
        if A[H - 1][col] != B[H - 1][col]:
            print("No")
            return
    print("Yes")
    print(change_num)


if __name__ == "__main__":
    # debug_input()
    main()
