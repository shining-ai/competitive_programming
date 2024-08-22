import io
import sys

_INPUT = """\
15 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    prime_nums = [0] * (N + 1)
    for i in range(2, N + 1):
        if prime_nums[i] != 0:
            continue
        x = 1
        while i * x <= N:
            prime_nums[i * x] += 1
            x += 1
    over_k_num = 0
    for prime_num in prime_nums:
        if prime_num < K:
            continue
        over_k_num += 1
    print(over_k_num)


if __name__ == "__main__":
    # debug_input()
    main()
