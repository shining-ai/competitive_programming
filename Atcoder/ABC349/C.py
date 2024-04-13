import io
import sys


def debug_input():
    _INPUT = """\
snuke
RNG
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input().upper()
    T = input()
    check_flag = [False, False, False]
    current = 0
    while current < len(S):
        if S[current] == T[0]:
            check_flag[0] = True
            current += 1
            break
        current += 1
    while current < len(S):
        if S[current] == T[1]:
            check_flag[1] = True
            current += 1
            break
        current += 1
    while current < len(S):
        if S[current] == T[2]:
            check_flag[2] = True
            current += 1
            break
        current += 1
    if T[2] == "X":
        check_flag[2] = True
    if check_flag[0] and check_flag[1] and check_flag[2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
