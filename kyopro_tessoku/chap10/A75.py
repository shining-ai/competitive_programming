import io
import sys


def debug_input():
    _INPUT = """\
4
20 70
30 50
30 100
20 60
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    Exam = [list(map(int, input().split())) for _ in range(N)]

    Exam.sort(key=lambda x: x[1])

    DP = [[1 << 30] * (N + 1) for _ in range(N + 1)]
    DP[0][0] = 0

    for i in range(N):
        t, d = Exam[i]
        for j in range(i + 1):
            DP[i + 1][j] = min(DP[i + 1][j], DP[i][j])
            if DP[i][j] == 1 << 30:
                continue
            if DP[i][j] + t <= d:
                DP[i + 1][j + 1] = min(DP[i + 1][j + 1], DP[i][j] + t)

    for i in range(N, -1, -1):
        if DP[N][i] != 1 << 30:
            print(i)
            break


if __name__ == "__main__":
    # debug_input()
    main()
