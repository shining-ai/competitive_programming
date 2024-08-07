import io
import sys
from collections import defaultdict
import itertools

_INPUT = """\
4 6
1 1 1 1 1 2
1 2 2 2 2 2
1 2 2 3 2 3
1 2 3 2 2 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# Hが少ないので、Hについてbit全探索する
def main():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    max_grid = 0
    for i in range(1 << H):
        row_pattern = bin(i)[2:].zfill(H)
        counter = defaultdict(int)
        for w in range(W):
            value = -1
            for shift_bit, row in enumerate(row_pattern):
                if row == "0":
                    continue
                if value == -1:
                    value = grid[H - shift_bit - 1][w]
                if value != grid[H - shift_bit - 1][w]:
                    break
            else:
                counter[value] += row_pattern.count("1")
        counter[-1] = 0
        max_grid = max(max_grid, max(counter.values()))
    print(max_grid)


if __name__ == "__main__":
    # debug_input()
    main()
