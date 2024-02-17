import io
import sys


def debug_input():
    _INPUT = """\
13 16 9
ULURDLURD
################
##..##.#..####.#
###.#..#.....#.#
#..##..#####.###
#...#..#......##
###.##.#..#....#
##.#####....##.#
###.###.#.#.#..#
######.....##..#
#...#.#.######.#
##..###..#..#.##
#...#.#.#...#..#
################

    """

    sys.stdin = io.StringIO(_INPUT)


def check_route(h, w, T, S):
    for t in T:
        if t == "L":
            w -= 1
        elif t == "R":
            w += 1
        elif t == "U":
            h -= 1
        elif t == "D":
            h += 1
        if S[h][w] == "#":
            return False
    return True


def main():
    H, W, N = map(int, input().split())
    T = input()
    S = list(input() for _ in range(H))
    ans = 0

    for h in range(1, H - 1):
        for w in range(1, W - 1):
            if S[h][w] == "#":
                continue
            if check_route(h, w, T, S):
                ans += 1
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
