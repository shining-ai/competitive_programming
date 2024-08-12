import io
import sys

_INPUT = """\
192
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    K = int(input())
    factors = []
    abc_nums = 0
    for i in range(1, int(K**0.5) + 1):
        if K % i == 0:
            factors.append(i)
    for a in range(len(factors)):
        for b in range(a, len(factors)):
            if K % (factors[a] * factors[b]) != 0:
                continue
            c = K // (factors[a] * factors[b])
            if factors[a] <= factors[b] <= c:
                abc_nums += 1
    print(abc_nums)


if __name__ == "__main__":
    # debug_input()
    main()
