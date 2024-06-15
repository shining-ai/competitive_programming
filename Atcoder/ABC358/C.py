import io
import sys


def debug_input():
    _INPUT = """\
8 6
xxoxxo
xxoxxx
xoxxxx
xxxoxx
xxoooo
xxxxox
xoxxox
oxoxxo

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    S = [list(input()) for _ in range(N)]

    dp = [set() for _ in range(2**N)]
    for i, s in enumerate(S):
        for j in range(2**i):
            for num in dp[j]:
                dp[j + 2**i].add(num)
            for num, num_s in enumerate(s):
                if num_s == "o":
                    dp[j + 2**i].add(num)

    min_store = float("inf")
    for i, d in enumerate(dp):
        if len(d) == M:
            min_store = min(min_store, i.bit_count())
    print(min_store)


if __name__ == "__main__":
    # debug_input()
    main()
