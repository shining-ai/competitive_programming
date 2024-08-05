import io
import sys

_INPUT = """\
5 4
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# k k(k-1) k(k-1)(k-2) k(k-1)(k-2)**2
def main():
    N, K = map(int, input().split())
    if N == 1:
        print(K)
        return
    if K == 1:
        print(0)
        return
    if N == 2:
        print(K * (K - 1))
        return
    if K < 3:
        print(0)
        return

    def power(x, n):
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
                result %= 1000000007
            x *= x
            x %= 1000000007
            n //= 2
        return result

    pattern_num = K * (K - 1)
    pattern_num *= power(K - 2, N - 2)
    pattern_num %= 1000000007
    print(pattern_num)


if __name__ == "__main__":
    # debug_input()
    main()
