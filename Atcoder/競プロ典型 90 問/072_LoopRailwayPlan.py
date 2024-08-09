import io
import sys
import copy

sys.setrecursionlimit(12000)


_INPUT = """\
3 3
...
.#.
...
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# マス目が少ないので、全探索できる
# バックトラッキングとDFSを使う
def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    max_loop = 0
    seen = set()

    def check_loop(row, col, goal, step):
        nonlocal max_loop
        nonlocal start
        if not start:
            if (row, col) == goal:
                max_loop = max(max_loop, step)
                return
        start = False
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if not (0 <= row + dr < H and 0 <= col + dc < W):
                continue
            if C[row + dr][col + dc] == "#":
                continue
            if (row + dr, col + dc) in seen:
                continue
            seen.add((row + dr, col + dc))
            check_loop(row + dr, col + dc, goal, step + 1)
            seen.discard((row + dr, col + dc))

    for row in range(H):
        for col in range(W):
            if C[row][col] == "#":
                continue
            start = True
            check_loop(row, col, (row, col), 0)

    if max_loop <= 2:
        print(-1)
    else:
        print(max_loop)


if __name__ == "__main__":
    # debug_input()
    main()
