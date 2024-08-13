import io
import sys

_INPUT = """\
4 2
1 2 3 50
2 3 4 45
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, Q = map(int, input().split())
    conditions = [list(map(int, input().split())) for _ in range(Q)]
    for i in conditions:  # インデックスに修正
        i[0] -= 1
        i[1] -= 1
        i[2] -= 1

    all_pattern = 1
    for digit in range(60):  # 1桁ずつ調べる
        digit_way = 0
        for binary in range(2**N):  # digitビット目の値をbit全探索
            for x, y, z, w in conditions:
                if (binary >> x & 1 | binary >> y & 1 | binary >> z & 1) != (
                    w >> digit & 1
                ):
                    break
            else:
                digit_way += 1
        all_pattern *= digit_way
        all_pattern %= 10**9 + 7
    print(all_pattern)


if __name__ == "__main__":
    # debug_input()
    main()
