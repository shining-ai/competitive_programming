import io
import sys

_INPUT = """\
98 100
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def count_num(n):
    res = n * (n + 1) // 2
    res %= 1000000007
    return res


def main():
    L, R = map(int, input().split())
    ans = 0
    for char_num in range(len(str(L)), len(str(R)) + 1):
        right = min(R, 10 ** (char_num) - 1)
        left = max(L, 10 ** (char_num - 1)) - 1
        if left > right:
            continue
        num = count_num(right) - count_num(left)
        ans += num * char_num
        ans %= 1000000007
        if R <= right:
            break
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
