import io
import sys


def debug_input():
    _INPUT = """\
13 656320850
0100110011101
-900549713 -713494784 -713078652 -687818593 -517374932 -498415009 -472742091 -390030458 -379340552 -237481538 -44636942 352721061 695864366

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, T = map(int, input().split())
    S = input()
    X = list(map(int, input().split()))

    dir_rights = []
    dir_lefts = []
    for i, s in enumerate(S):
        if s == "1":
            dir_rights.append(X[i])
        else:
            dir_lefts.append(X[i])

    num = 0
    dir_rights.sort()
    dir_lefts.sort()
    dir_lefts.append(float("inf"))
    left = 0
    right = 0
    for r_ant in dir_rights:
        while dir_lefts[left] <= r_ant:
            left += 1
        while dir_lefts[right] <= r_ant + 2*T:
            right += 1
        num += right - left
    print(num)


if __name__ == "__main__":
    # debug_input()
    main()
