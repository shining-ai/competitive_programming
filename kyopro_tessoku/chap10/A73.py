import heapq
import io
import sys


def debug_input():
    _INPUT = """\
3 3
1 2 70 1
2 3 20 1
1 3 90 0
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    net = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b, c, d = map(int, input().split())
        net[a].append([b, 10000 * c - d])
        net[b].append([a, 10000 * c - d])

    kakutei = [False] * (N + 1)
    cur = [1 << 61] * (N + 1)
    cur[1] = 0
    Q = [(0, 1)]
    heapq.heapify(Q)

    while Q:
        pos = heapq.heappop(Q)[1]
        if kakutei[pos]:
            continue
        kakutei[pos] = True
        for next_pos, cost in net[pos]:
            if cur[next_pos] > cur[pos] + cost:
                cur[next_pos] = cur[pos] + cost
                heapq.heappush(Q, (cur[next_pos], next_pos))

    if cur[N] == 1 << 61:
        print(-1)
    else:
        print(1 + cur[N] // 10000, (10000 - cur[N] % 10000))


if __name__ == "__main__":
    # debug_input()
    main()
