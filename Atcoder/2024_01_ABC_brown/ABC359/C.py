import io
import sys


def debug_input():
    _INPUT = """\
3 1
4 1
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    move_x = T[0] - S[0]
    move_y = T[1] - S[1]
    if abs(move_x) <= abs(move_y):
        print(abs(move_y))
        return
    ans = abs(move_y)
    ans += (abs(move_x) - abs(move_y) - 1) // 2

    if 0 <= S[0]:
        if (S[0] + S[1]) % 2 == 0:
            if S[0] < T[0]:
                if (move_x - move_y) % 2 == 0:
                    ans += 1
            if S[0] > T[0]:
                ans += 1
        else:
            if S[0] < T[0]:
                ans += 1
            if S[0] > T[0]:
                if (move_x - move_y) % 2 == 0:
                    ans += 1
    else:  # マイナススタート
        if (S[0] + S[1]) % 2 == 0:
            if S[0] < T[0]:
                if (move_x - move_y) % 2 == 0:
                    ans += 1
            if S[0] > T[0]:
                ans += 1
        else:
            if S[0] < T[0]:
                ans += 1
            if S[0] > T[0]:
                if (move_x - move_y) % 2 == 0:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
