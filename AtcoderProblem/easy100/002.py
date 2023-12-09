import io
import sys


def debug_input():
    _INPUT = """\
2
1 4
    """

    sys.stdin = io.StringIO(_INPUT)


# 計算量: O(N!)
def main():
    N = int(input())
    X = list(map(int, input().split()))

    ans = 10**9
    for p in range(1, 101):
        sum_stamina = 0
        for i_x in X:
            sum_stamina += (i_x - p) ** 2

        ans = min(ans, sum_stamina)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
