import io
import sys
from itertools import combinations
from bisect import bisect_left

_INPUT = """\
5 2 10
3 8 7 5 11
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K, P = map(int, input().split())
    A = list(map(int, input().split()))
    before_half = A[: N // 2]
    after_half = A[N // 2 :]
    before_half_price = [[] for _ in range(K + 1)]
    after_half_price = [[] for _ in range(K + 1)]

    def all_search(arr, price_list):
        for i in range(K + 1):
            for comb in combinations(arr, i):
                price = sum(comb)
                price_list[i].append(price)
            price_list[i].sort()

    all_search(before_half, before_half_price)
    all_search(after_half, after_half_price)
    ans = 0
    for i in range(K + 1):
        for price in before_half_price[i]:
            remain = P - price
            index = bisect_left(after_half_price[K - i], remain + 1)
            ans += index
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
