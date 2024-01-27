import collections
import io
import sys


def debug_input():
    _INPUT = """\
2
800 300
100 100
200 10


    """

    sys.stdin = io.StringIO(_INPUT)


def calc_cookable_num(stock, receipe):
    material = len(stock)
    cookable_num = float("inf")
    for i in range(material):
        if receipe[i] == 0:
            continue
        cookable_num = min(stock[i] // receipe[i], cookable_num)

    return cookable_num


def main():
    N = int(input())
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    a_max = calc_cookable_num(Q, A)
    ans = a_max

    for i in range(a_max + 1):
        stock = Q.copy()
        for j in range(N):
            stock[j] -= i * A[j]
        b_max = calc_cookable_num(stock, B)

        ans = max(ans, i + b_max)

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
