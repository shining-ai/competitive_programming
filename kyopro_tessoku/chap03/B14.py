import bisect
import io
import sys


def debug_input():
    _INPUT = """\
6 30
5 1 18 7 2 9
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    def Enumerate(A):
        SumList = []
        for i in range(2 ** len(A)):
            sum = 0  # 現在の合計値
            for j in range(len(A)):
                wari = 2**j
                if (i // wari) % 2 == 1:
                    sum += A[j]
            SumList.append(sum)
        return SumList

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    L1 = A[0 : N // 2]
    L2 = A[N // 2 : N]

    comb_l1 = Enumerate(L1)
    comb_l2 = Enumerate(L2)
    comb_l1.sort()
    comb_l2.sort()

    ans = "No"

    for i in range(len(comb_l1)):
        pos = bisect.bisect_left(comb_l2, K - comb_l1[i])
        if pos < len(comb_l2) and comb_l2[pos] == K - comb_l1[i]:
            if pos < len(comb_l2) and comb_l2[pos] == K - comb_l1[i]:
                ans = "Yes"
                break

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
