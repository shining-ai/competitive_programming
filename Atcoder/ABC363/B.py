import io
import sys
import heapq


_INPUT = """\
5 10 3
3 11 1 6 2
"""


def debug_input():

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, T, P = map(int, input().split())
    L = list(map(int, input().split()))
    L = [-x for x in L]

    heapq.heapify(L)
    num = 0
    day = 0
    while num < P:
        current = -heapq.heappop(L)
        if current >= T - day:
            num += 1
            continue
        day = T - current
        num += 1
    print(day)


if __name__ == "__main__":
    # debug_input()
    main()
