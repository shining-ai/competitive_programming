import io
import sys

_INPUT = """\
2
1 2
3 4
5 6
7 8
2
1 2 2 2 1 1
2 2 1 2 1 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(N)]

    prefix_sum = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                prefix_sum[x][y][z] = (
                    A[x - 1][y - 1][z - 1]
                    + prefix_sum[x - 1][y][z]
                    + prefix_sum[x][y - 1][z]
                    + prefix_sum[x][y][z - 1]
                    - prefix_sum[x - 1][y - 1][z]
                    - prefix_sum[x - 1][y][z - 1]
                    - prefix_sum[x][y - 1][z - 1]
                    + prefix_sum[x - 1][y - 1][z - 1]
                )

    Q = int(input())
    for _ in range(Q):
        Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
        ans = (
            prefix_sum[Rx][Ry][Rz]
            - prefix_sum[Lx - 1][Ry][Rz]
            - prefix_sum[Rx][Ly - 1][Rz]
            - prefix_sum[Rx][Ry][Lz - 1]
            + prefix_sum[Lx - 1][Ly - 1][Rz]
            + prefix_sum[Rx][Ly - 1][Lz - 1]
            + prefix_sum[Lx - 1][Ry][Lz - 1]
            - prefix_sum[Lx - 1][Ly - 1][Lz - 1]
        )
        print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
