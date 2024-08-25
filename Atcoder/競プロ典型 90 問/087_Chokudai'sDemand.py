import io
import sys
import copy

_INPUT = """\
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, P, K = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(N)]
    RIGHT_INIT = 5 * 10**9

    def count_under_P(fee):
        distances = copy.deepcopy(costs)
        for start in range(N):
            for end in range(N):
                if distances[start][end] == -1:
                    distances[start][end] = fee

        for relay in range(N):
            for start in range(N):
                for end in range(N):
                    distances[start][end] = min(
                        distances[start][end],
                        distances[start][relay] + distances[relay][end],
                    )

        count = 0
        for start in range(N):
            for end in range(start + 1, N):
                if distances[start][end] > P:
                    continue
                count += 1
        return count

    # 該当する先頭の要素を探す
    def search_border_left(K):
        left = 1
        right = RIGHT_INIT
        while left < right:
            fee = (left + right) // 2
            under_P_num = count_under_P(fee)
            if K < under_P_num:
                left = fee + 1
            else:
                right = fee
        return left

    def search_border_right(K):
        left = 1
        right = RIGHT_INIT
        while left < right:
            fee = (left + right) // 2
            under_P_num = count_under_P(fee)
            if K <= under_P_num:
                left = fee + 1
            else:
                right = fee
        return left

    min_cost = search_border_left(K)
    # max_cost = search_border_left(K - 1)
    max_cost = search_border_right(K)
    cost = max_cost - min_cost
    if cost >= 2 * 10**9:
        print("Infinity")
    else:
        print(cost)


if __name__ == "__main__":
    # debug_input()
    main()
