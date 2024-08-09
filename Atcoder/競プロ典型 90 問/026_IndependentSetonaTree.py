import io
import sys
from collections import defaultdict, deque

_INPUT = """\
4
1 2
2 3
2 4
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    network = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    even = []
    odd = []
    seen = set()
    queue = deque([(1, 0)])
    while queue:
        node, depth = queue.popleft()
        if depth % 2 == 0:
            even.append(node)
        else:
            odd.append(node)
        seen.add(node)
        for neighbor in network[node]:
            if neighbor in seen:
                continue
            queue.append((neighbor, depth + 1))

    if len(even) >= N // 2:
        print(*even[: N // 2])
    else:
        print(*odd[: N // 2])


if __name__ == "__main__":
    # debug_input()
    main()
