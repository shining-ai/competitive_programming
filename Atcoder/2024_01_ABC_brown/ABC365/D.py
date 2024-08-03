import io
import sys

_INPUT = """\
6
PRSSRS
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def judge(me, you):
    if me == "R":
        if you == "S":
            return 1
        elif you == "P":
            return -1
        else:
            return 0
    elif me == "S":
        if you == "P":
            return 1
        elif you == "R":
            return -1
        else:
            return 0
    else:
        if you == "R":
            return 1
        elif you == "S":
            return -1
        else:
            return 0


def main():
    N = int(input())
    S = input()
    R_max_wins = [0] * (N + 1)
    S_max_wins = [0] * (N + 1)
    P_max_wins = [0] * (N + 1)

    for i, s in enumerate(S):
        if s == "R":
            R_max_wins[i + 1] = max(S_max_wins[i], P_max_wins[i])
            S_max_wins[i + 1] = 0
            P_max_wins[i + 1] = max(R_max_wins[i], S_max_wins[i]) + 1
        elif s == "S":
            R_max_wins[i + 1] = max(S_max_wins[i], P_max_wins[i]) + 1
            S_max_wins[i + 1] = max(R_max_wins[i], P_max_wins[i])
            P_max_wins[i + 1] = 0
        else:  # P
            R_max_wins[i + 1] = 0
            S_max_wins[i + 1] = max(R_max_wins[i], P_max_wins[i]) + 1
            P_max_wins[i + 1] = max(R_max_wins[i], S_max_wins[i])
    print(max(R_max_wins[N], S_max_wins[N], P_max_wins[N]))


if __name__ == "__main__":
    # debug_input()
    main()
