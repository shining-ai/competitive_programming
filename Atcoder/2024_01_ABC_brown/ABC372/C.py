import io
import sys

_INPUT = """\
15 10
BBCCBCACCBACACA
9 C
11 B
5 B
11 B
4 A
8 C
8 B
5 B
7 B
14 B
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    S = list(input())
    ABC_num = 0
    for i in range(len(S) - 2):
        if S[i] == "A" and S[i + 1] == "B" and S[i + 2] == "C":
            ABC_num += 1

    def is_ABC(index):
        if S[index] == "A":
            if not (index + 2 < len(S)):
                return False
            if S[index + 1] == "B" and S[index + 2] == "C":
                return True
            return False
        elif S[index] == "B":
            if not (0 <= index - 1 and index + 1 < len(S)):
                return False
            if S[index - 1] == "A" and S[index + 1] == "C":
                return True
            return False
        elif S[index] == "C":
            if not (0 <= index - 2):
                return False
            if S[index - 2] == "A" and S[index - 1] == "B":
                return True
            return False

    for _ in range(Q):
        X, C = input().split()
        X = int(X) - 1
        if S[X] == C:
            print(ABC_num)
            continue
        if is_ABC(X):
            ABC_num -= 1
        S[X] = C
        if C == "A":
            if not (X + 2 < len(S)):
                print(ABC_num)
                continue
            if S[X + 1] == "B" and S[X + 2] == "C":
                ABC_num += 1
        elif C == "B":
            if not (0 <= X - 1 and X + 1 < len(S)):
                print(ABC_num)
                continue
            if S[X - 1] == "A" and S[X + 1] == "C":
                ABC_num += 1
        elif C == "C":
            if not (0 <= X - 2):
                print(ABC_num)
                continue
            if S[X - 2] == "A" and S[X - 1] == "B":
                ABC_num += 1
        print(ABC_num)


if __name__ == "__main__":
    # debug_input()
    main()
