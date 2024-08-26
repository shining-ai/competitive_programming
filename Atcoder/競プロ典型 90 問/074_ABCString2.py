import io
import sys

_INPUT = """\
3
aba
"""


# baaa -> 1
# abaa -> 2
# aaba -> 4
# aaab -> 8
def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = input()
    ans = 0
    for i, c in enumerate(S):
        if c == "a":
            d = 0
        elif c == "b":
            d = 1
        else:
            d = 2

        ans += (2**i) * d
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
