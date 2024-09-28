import io
import sys
from collections import defaultdict
from math import inf

_INPUT = """\
4 2
2 1 5
3 4 -3

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    network = defaultdict(list)
    for _ in range(M):
        u, v, c = map(int, input().split())
        network[u].append((v, c))
        network[v].append((u, -c))

    ans = [0] * (N + 1)
    seen = set()
    for i in range(1, N + 1):
        if i in seen:
            continue
        stack = [i]
        seen.add(i)
        while stack:
            node = stack.pop()
            for next_node, cost in network[node]:
                if next_node in seen:
                    continue
                seen.add(next_node)
                ans[next_node] = ans[node] + cost
                stack.append(next_node)
    ans = ans[1:]
    min_val = min(ans)
    if min_val < -(10**18):
        offset = -(10**18) - min_val
        for i in range(N):
            ans[i] += offset
    if max(ans) > 10**18:
        offset = 10**18 - max(ans)
        for i in range(N):
            ans[i] += offset
    for i in range(N):
        print(ans[i], end=" ")
    print()


if __name__ == "__main__":
    # debug_input()
    main()
