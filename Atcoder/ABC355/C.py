import io
import sys


def debug_input():
    _INPUT = """\
3 5
4 2 9 7 5

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    turn = 0
    # field = [[0] * N for _ in range(N)]
    row_count = [0] * N
    col_count = [0] * N
    right_down_count = 0
    left_down_count = 0
    for a in A:
        turn += 1
        row = (a - 1) // N
        col = (a - 1) % N
        row_count[row] += 1
        col_count[col] += 1
        if row == col:
            right_down_count += 1
        if row + col == N - 1:
            left_down_count += 1

        if row_count[row] == N or col_count[col] == N:
            print(turn)
            return
        if right_down_count == N or left_down_count == N:
            print(turn)
            return

    print(-1)


if __name__ == "__main__":
    # debug_input()
    main()
