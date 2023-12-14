import io
import sys


def debug_input():
    _INPUT = """\
60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A = [list(map(int, input().split())) for _ in range(3)]

    for _ in range(int(input())):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if A[i][j] == b:
                    A[i][j] = 0

    ans = "No"
    for i in range(3):
        if A[i][0] == 0 and A[i][1] == 0 and A[i][2] == 0:
            ans = "Yes"
        elif A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
            ans = "Yes"

    if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
        ans = "Yes"
    elif A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
        ans = "Yes"
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
