import io
import sys

_INPUT = """\
2
1 1 3 2
2 1 4 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    grid = [[0] * 1002 for _ in range(1002)]
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        grid[ly][lx] += 1
        grid[ly][rx] -= 1
        grid[ry][lx] -= 1
        grid[ry][rx] += 1

    for row in range(1001):
        for col in range(1001):
            grid[row][col + 1] += grid[row][col]

    for col in range(1001):
        for row in range(1001):
            grid[row + 1][col] += grid[row][col]

    thicks = [0] * (N + 1)
    for row in range(1001):
        for col in range(1001):
            thicks[grid[row][col]] += 1

    for thick in thicks[1:]:
        print(thick)


if __name__ == "__main__":
    # debug_input()
    main()
