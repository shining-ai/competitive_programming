import io
import sys

"""
G#G..
.G...
G#GG#
"""


def debug_input():
    _INPUT = """\
3 3
..#
#..
..#

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    max_area = 0

    def change_next_S(S, h, w):
        nonlocal max_area
        if h + 1 < H and S[h + 1][w] == ".":
            S[h + 1][w] = "G"
            max_area = 1
        if h - 1 >= 0 and S[h - 1][w] == ".":
            S[h - 1][w] = "G"
            max_area = 1
        if w + 1 < W and S[h][w + 1] == ".":
            S[h][w + 1] = "G"
            max_area = 1
        if w - 1 >= 0 and S[h][w - 1] == ".":
            S[h][w - 1] = "G"
            max_area = 1

    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                change_next_S(S, h, w)

    seen = set()
    G_pos = []
    for h in range(H):
        for w in range(W):
            if (h, w) in seen:
                continue
            if S[h][w] != ".":
                continue
            area = 1
            stack = [(h, w)]
            seen.add((h, w))
            while G_pos:
                gh, gw = G_pos.pop()
                seen.remove((gh, gw))

            while stack:
                sh, sw = stack.pop()
                for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nh, nw = sh + dh, sw + dw
                    if not (0 <= nh < H and 0 <= nw < W):
                        continue
                    if (nh, nw) in seen:
                        continue
                    if S[nh][nw] == ".":
                        area += 1
                        stack.append((nh, nw))
                        seen.add((nh, nw))
                    elif S[nh][nw] == "G":
                        area += 1
                        seen.add((nh, nw))
                        G_pos.append((nh, nw))
            max_area = max(max_area, area)
    print(max_area)


if __name__ == "__main__":
    # debug_input()
    main()
