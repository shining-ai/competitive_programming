import io
import sys

_INPUT = """\
3 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, L = map(int, input().split())
    patterns = [1] * L
    for i in range(L, N+1):
        pattern = patterns[i-1] + patterns[i-L]
        patterns.append(pattern % 1000000007)

    print(patterns[-1])


if __name__ == "__main__":
    # debug_input()
    main()
