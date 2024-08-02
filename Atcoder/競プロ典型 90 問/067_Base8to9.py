import io
import sys

_INPUT = """\
1330 1
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())

    def base_8_to_10(n):
        base_10 = 0
        digit = 0
        while n:
            base_10 += (n % 10) * (8**digit)
            digit += 1
            n //= 10
        return base_10

    def base_10_to_9(n):
        base_9 = 0
        digit = 0
        while n > 0:
            bit = n % 9
            base_9 += bit * (10**digit)
            n = n // 9
            digit += 1
        return base_9

    for _ in range(K):
        N = base_8_to_10(N)
        N = base_10_to_9(N)
        N = int(str(N).replace("8", "5"))

    print(N)


if __name__ == "__main__":
    # debug_input()
    main()
