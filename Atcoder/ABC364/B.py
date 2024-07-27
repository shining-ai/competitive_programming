import io
import sys


_INPUT = """\
2 3
2 1
.#.
...
ULDRU
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    S = list(map(int, input().split()))
    C = [list(input()) for _ in range(H)]
    X = input()

    def can_move(x, y):
        if not (0 < x <= W and 0 < y <= H):
            return False
        if C[y-1][x-1] == "#":
            return False
        return True

    for x in X:
        if x == "U":
            if can_move(S[1], S[0] - 1):
                S[0] -= 1
        elif x == "D":
            if can_move(S[1], S[0] + 1):
                S[0] += 1
        elif x == "L":
            if can_move(S[1] - 1, S[0]):
                S[1] -= 1
        elif x == "R":
            if can_move(S[1] + 1, S[0]):
                S[1] += 1
    print(S[0], S[1])


if __name__ == "__main__":
    # debug_input()
    main()
