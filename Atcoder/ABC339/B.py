import io
import sys


def debug_input():
    _INPUT = """\
3 4 5
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W, N = map(int, input().split())
    field = [["."] * W for _ in range(H)]
    curr = (0, 0)
    direction_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0
    for _ in range(N):
        if field[curr[0]][curr[1]] == ".":
            field[curr[0]][curr[1]] = "#"
            direction_index = (direction_index + 1) % 4
        else:
            field[curr[0]][curr[1]] = "."
            direction_index = (direction_index + 3) % 4
        curr = (
            (curr[0] + direction_list[direction_index][0]) % H,
            (curr[1] + direction_list[direction_index][1]) % W,
        )

    for row in field:
        print("".join(row))


if __name__ == "__main__":
    # debug_input()
    main()
