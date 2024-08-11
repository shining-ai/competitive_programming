import io
import sys
from collections import deque, defaultdict

_INPUT = """\
3 3
1 1
3 3
..#
#.#
#..
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    start = (start[0] - 1, start[1] - 1)
    goal = (goal[0] - 1, goal[1] - 1)
    S = [input() for _ in range(H)]
    queue = deque(
        [
            ((start[0] - 1, start[1]), "up", 0),
            ((start[0] + 1, start[1]), "down", 0),
            ((start[0], start[1] - 1), "left", 0),
            ((start[0], start[1] + 1), "right", 0),
        ]
    )
    turn_nums = defaultdict(lambda: float("inf"))
    turn_nums = [[float("inf")] * W for _ in range(H)]

    while queue:
        (h, w), dir, turn_num = queue.popleft()
        if not (0 <= h < H and 0 <= w < W):
            continue
        if S[h][w] == "#":
            continue
        if turn_nums[h][w] < turn_num:
            continue
        turn_nums[h][w] = turn_num
        if (h, w) == goal:
            break
        pre_dir = dir

        dirs = [("up", (-1, 0)), ("down", (1, 0)), ("left", (0, -1)), ("right", (0, 1))]
        for dir, (dh, dw) in dirs:
            if not (0 <= h + dh < H and 0 <= w + dw < W):
                continue
            if dir == pre_dir:
                queue.appendleft(((h + dh, w + dw), dir, turn_num))
            else:
                queue.append(((h + dh, w + dw), dir, turn_num + 1))

    print(turn_nums[goal[0]][goal[1]])


if __name__ == "__main__":
    # debug_input()
    main()
