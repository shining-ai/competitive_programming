import io
import sys
from collections import deque

_INPUT = """\
227
21 47 56
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# queueを使った解法(TLE O(N**3))
# def main():
# N = int(input())
# coins = list(map(int, input().split()))
# seen = set([N])
# queue = deque([(N, 0)])
# while queue:
#     remain, coin_num = queue.popleft()
#     if remain == 0:
#         print(coin_num)
#         return
#     for coin in coins:
#         if remain - coin in seen:
#             continue
#         if remain - coin < 0:
#             continue
#         queue.append((remain - coin, coin_num + 1))
#         seen.add(remain - coin)


def main():
    N = int(input())
    A, B, C = map(int, input().split())
    min_coin_num = 10000
    for a_num in range(10000):
        for b_num in range(10000):
            remain = N - a_num * A - b_num * B
            if remain < 0:
                break
            if remain % C != 0:
                continue
            min_coin_num = min(min_coin_num, (a_num + b_num + remain // C))
    print(min_coin_num)


if __name__ == "__main__":
    # debug_input()
    main()
