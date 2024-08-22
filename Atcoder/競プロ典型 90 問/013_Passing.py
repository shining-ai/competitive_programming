import io
import sys
from heapq import heappush, heappop

_INPUT = """\
7 9
1 2 2
1 3 3
2 5 2
3 4 1
3 5 4
4 7 5
5 6 1
5 7 6
6 7 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# startとgoalの2パターンの最短距離をダイクストラ法で求める
def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A - 1].append((B, C))
        graph[B - 1].append((A, C))

    def search_min_diatance(start):
        min_heap = [(0, start)]
        distance_from_start = [float("inf")] * N
        distance_from_start[start] = 0
        done = set()
        while min_heap:
            cost, node = heappop(min_heap)
            if node in done:
                continue
            done.add(node)
            distance_from_start[node] = cost
            for next_node, next_cost in graph[node]:
                heappush(min_heap, (cost + next_cost, next_node - 1))
        return distance_from_start

    distance_from_zero = search_min_diatance(0)
    distance_from_N = search_min_diatance(N - 1)

    for i in range(N):
        print(distance_from_zero[i] + distance_from_N[i])


if __name__ == "__main__":
    # debug_input()
    main()
