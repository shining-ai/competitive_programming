import io
import sys

_INPUT = """\
3
abc
de
fghi
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    max_len = 0
    for i in range(N):
        max_len = max(max_len, len(S[i]))
    T = [[] for _ in range(max_len)]
    for i in range(len(S[0])):
        T[i].append(S[0][i])

    for s in S[1:]:
        for i in range(max_len):
            if len(s) <= i:
                if not T[i]:
                    continue
                T[i].append("*")
            else:
                T[i].append(s[i])

    for t in T:
        print("".join(reversed(t)))



if __name__ == "__main__":
    # debug_input()
    main()
