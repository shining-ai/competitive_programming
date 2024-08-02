import io
import sys

_INPUT = """\
6 7 1
1 2 3 4 5 6
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        A_i = A[i] % P
                        A_j = A[j] % P
                        A_k = A[k] % P
                        A_l = A[l] % P
                        A_m = A[m] % P
                        if A_i * A_j % P * A_k % P * A_l % P * A_m % P == Q:
                            ans += 1
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
