import io
import sys

_INPUT = """\
3 3
1 1 1
1 1 2
1 1 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    row_sums = [sum(row) for row in A]
    col_sums = []
    for i in range(W):
        col_sum = 0
        for j in range(H):
            col_sum += A[j][i]
        col_sums.append(col_sum)

    for row in range(H):
        for col in range(W):
            print(row_sums[row] + col_sums[col] - A[row][col], end=" ")
        print()


if __name__ == "__main__":
    # debug_input()
    main()
