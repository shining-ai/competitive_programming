import io
import sys

_INPUT = """\
5 77
1 16
3 91
43 9
4 26
23 11

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, S = map(int, input().split())
    sums = [[False] * (S + 1) for _ in range(N + 1)]
    sums[0][0] = ""
    for i in range(1, N + 1):
        A, B = map(int, input().split())
        for j in range(S):
            if sums[i - 1][j] == False:
                continue
            if j + A <= S:
                sums[i][j + A] = sums[i - 1][j] + "A"
            if j + B <= S:
                sums[i][j + B] = sums[i - 1][j] + "B"
    if sums[N][S] == False:
        print("Impossible")
        return
    print(sums[N][S])

    # ListにappendしていくとTLEする
    # rests = [(S, "")]
    # for i in range(N):
    #     if not rests:
    #         print("Inpossible")
    #         return
    #     A, B = map(int, input().split())
    #     next_rests = []
    #     for rest, combination in rests:
    #         if rest - A >= 0:
    #             next_rests.append((rest - A, combination + "A"))
    #         if rest - B >= 0:
    #             next_rests.append((rest - B, combination + "B"))
    #     rests = next_rests

    # for rest, combination in rests:
    #     if rest == 0:
    #         print(combination)
    #         return
    # print("Impossible")


if __name__ == "__main__":
    debug_input()
    main()
