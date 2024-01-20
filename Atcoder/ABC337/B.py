import io
import sys


def debug_input():
    _INPUT = """\
AAABBBCCCCCCC
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = input()
    S_len = len(S)
    cnt = 0

    for i in range(S_len):
        if S[i] == "A":
            cnt += 1
        else:
            break

    for i in range(cnt, S_len):
        if S[i] == "B":
            cnt += 1
        else:
            break

    for i in range(cnt, S_len):
        if S[i] == "C":
            cnt += 1
        else:
            break

    if cnt == S_len:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # debug_input()
    main()
