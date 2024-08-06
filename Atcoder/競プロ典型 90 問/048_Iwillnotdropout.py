import io
import sys
import heapq

_INPUT = """\
4 3
4 3
9 5
15 8
8 6
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    max_heap = []
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        heapq.heappush(max_heap, (-b, i))
        A.append(a)

    max_point = 0
    for minit in range(K):
        point, q_num = heapq.heappop(max_heap)
        max_point += -point
        if q_num == -1:
            continue
        heapq.heappush(max_heap, (-(A[q_num] + point), -1))
    print(max_point)


if __name__ == "__main__":
    # debug_input()
    main()
