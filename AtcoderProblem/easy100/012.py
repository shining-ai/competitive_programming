import io
import sys


def debug_input():
    _INPUT = """\
20 3
0 5 15
    """

    sys.stdin = io.StringIO(_INPUT)


# 隣り合う点の長さを求め、最大のものを間引いたものが答えとなる
# 最後の点と最初の点の長さを求めるときに注意が必要
def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    distance = []

    for i in range(N):
        if i == N - 1:
            distance.append((K + A[0]) - A[i])
        else:
            distance.append(A[i + 1] - A[i])

    print(K - max(distance))


if __name__ == "__main__":
    # debug_input()
    main()
