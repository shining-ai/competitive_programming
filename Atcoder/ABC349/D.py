import io
import sys


def debug_input():
    _INPUT = """\
0 5
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    L, R = map(int, input().split())
    ans = []

    def lowest_bit_pos(n):
        if n == 0:
            return -1
        pos = 0
        while n & 1 == 0:
            n = n >> 1
            pos += 1
        return pos

    def highest_bit_pos(n):
        pos = 0
        while n > 0:
            n = n >> 1
            pos += 1
        return pos

    if L == 0:
        L = 2 ** (highest_bit_pos(R)-1)
        ans.append((0, L))

    while L < R:
        kouho = lowest_bit_pos(L)
        while L + 2**kouho > R:
            kouho -= 1
        after_L = L + 2**kouho
        ans.append((L, after_L))
        L = after_L

    print(len(ans))
    for a in ans:
        print(a[0], a[1])

if __name__ == "__main__":
    # debug_input()
    main()
