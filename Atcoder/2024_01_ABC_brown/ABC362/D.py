import io
import sys
import collections
import heapq

_INPUT = """\
5 8
928448202 994752369 906965437 942744902 907560126
2 5 975090662
1 2 908843627
1 5 969061140
3 4 964249326
2 3 957690728
2 4 942986477
4 5 948404113
1 3 988716403

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    cost_from_1 = [float("inf")] * (N + 1)
    graph = collections.defaultdict(set)
    for i in range(M):
        u, v, b = map(int, input().split())
        graph[u].add((v, b + A[v]))
        graph[v].add((u, b + A[u]))

    min_heap = [(A[1], 1)]
    done = set()
    while min_heap:
        cost, edge = heapq.heappop(min_heap)
        if edge in done:
            continue
        cost_from_1[edge] = cost
        done.add(edge)
        for next_edge, fee in graph[edge]:
            heapq.heappush(min_heap, (cost + fee, next_edge))

    for i in range(2, N + 1):
        print(cost_from_1[i], end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
