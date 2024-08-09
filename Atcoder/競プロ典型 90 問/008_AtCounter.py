import io
import sys

_INPUT = """\
10
attcordeer
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    TARGET_WORD = "atcoder"
    N = int(input())
    S = input()

    # pattern_until[TARGETのi文字目まで][Sのj文字目まで]: 方法の数
    pattern_until = [[0] * (N + 1) for _ in range(len(TARGET_WORD) + 1)]
    for j in range(N + 1):
        pattern_until[0][j] = 1
    for i in range(len(TARGET_WORD)):
        for j in range(len(S)):
            pattern_until[i + 1][j + 1] = pattern_until[i + 1][j]
            if TARGET_WORD[i] == S[j]:
                pattern_until[i + 1][j + 1] += pattern_until[i][j]
            pattern_until[i + 1][j + 1] %= 10**9 + 7
    print(pattern_until[-1][-1])


if __name__ == "__main__":
    # debug_input()
    main()
