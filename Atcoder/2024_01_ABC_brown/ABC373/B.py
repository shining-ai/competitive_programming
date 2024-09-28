import io
import sys
from collections import defaultdict

_INPUT = """\
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    key_pos = defaultdict(int)
    for i, c in enumerate(S):
        key_pos[c] = i + 1
    cost = 0
    current = key_pos["A"]
    for target in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cost += abs(current - key_pos[target])
        current = key_pos[target]
    print(cost)



if __name__ == "__main__":
    # debug_input()
    main()
