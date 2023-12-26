import heapq
import io
import sys


def debug_input():
    _INPUT = """\
6 7
1 2 15
1 4 20
2 3 65
2 5 4
3 6 50
4 5 30
5 6 8

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
    back = [0] * (N + 1)
    ans = []

    while q:
        cost, pos = heapq.heappop(q)
        if cur[pos] < cost:
            continue
        for next_pos, next_cost in net[pos]:
            if cur[next_pos] > cost + next_cost:
                cur[next_pos] = cost + next_cost
                back[next_pos] = pos
                heapq.heappush(q, ((cur[next_pos], next_pos)))

    if cur[N] == 1 << 61:
        print(-1)
    else:
        while N > 0:
            ans.append(N)
            N = back[N]

    for i in reversed(ans):
        print(i, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
