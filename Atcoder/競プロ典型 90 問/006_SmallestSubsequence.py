import io
import sys
from collections import defaultdict, deque

_INPUT = """\
14 5
kittyonyourlap
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    S = input().strip()
    char_to_index = defaultdict(deque)
    for i, c in enumerate(S):
        char_to_index[c].append(i)
    i = 0
    for current in range(K):
        for c in sorted(char_to_index.keys()):
            while char_to_index[c] and char_to_index[c][0] < i:
                char_to_index[c].popleft()
            if char_to_index[c] and char_to_index[c][0] + K - current <= N:
                print(c, end="")
                i = char_to_index[c].popleft()
                break
    print()


if __name__ == "__main__":
    # debug_input()
    main()
