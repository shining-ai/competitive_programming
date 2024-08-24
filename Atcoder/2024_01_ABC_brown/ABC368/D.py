import io
import sys
from collections import deque

_INPUT = """\
7 3
1 2
1 3
2 4
2 5
3 6
3 7
1 3 5
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    network = [set() for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        network[a].add(b)
        network[b].add(a)
    V = set(map(int, input().split()))
    V = set([v - 1 for v in V])

    connect_nums = [len(s) for s in network]
    stack = []
    for i, connect_num in enumerate(connect_nums):
        if connect_num == 1:
            stack.append(i)

    ans = N
    while stack:
        node = stack.pop()
        if node in V:
            continue
        next_node = network[node].pop()
        network[next_node].discard(node)
        ans -= 1
        if len(network[next_node]) == 1:
            stack.append(next_node)
    print(ans)


if __name__ == "__main__":
    debug_input()
    main()
