import io
import sys


def debug_input():
    _INPUT = """\
3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100

    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        A = list(map(int, input().split()))
        res = C
        for j in range(M):
           res += A[j] * B[j]
        if res > 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
