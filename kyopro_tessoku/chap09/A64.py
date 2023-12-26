import heapq
import io
import sys


def debug_input():
    _INPUT = """\
15 30
10 11 23
11 13 24
5 8 22
10 15 18
12 14 15
2 10 11
4 7 15
5 7 15
7 9 8
8 12 1
5 14 1
10 14 17
10 12 11
8 10 6
7 14 28
6 9 1
1 10 19
4 5 4
9 10 21
7 10 21
4 10 29
5 10 8
4 14 8
11 12 24
10 13 13
3 10 1
5 12 24
2 15 23
6 10 18
6 15 25

    """
    sys.stdin = io.StringIO(_INPUT)


# O(N)
def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]

    net = [[] for _ in range(N + 1)]
    for a, b, c in edges:
        net[a].append((b, c))
        net[b].append((a, c))

    cur = [1 << 61] * (N + 1)
    cur[1] = 0
    q = [(0, 1)]
    heapq.heapify(q)

    while q:
        cost, pos = heapq.heappop(q)
        if cur[pos] < cost:
            continue
        for next_pos, next_cost in net[pos]:
            if cur[next_pos] > cost + next_cost:
                cur[next_pos] = cost + next_cost
                heapq.heappush(q, ((cur[next_pos], next_pos)))

    for i in range(1, N + 1):
        if cur[i] == 1 << 61:
            print(-1)
        else:
            print(cur[i])


if __name__ == "__main__":
    # debug_input()
    main()
