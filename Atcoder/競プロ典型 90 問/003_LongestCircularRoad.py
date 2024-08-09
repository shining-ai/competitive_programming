import io
import sys
from collections import defaultdict

_INPUT = """\
10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10
"""


# 1 -> 2 -> 4 -> 5
#             -> 6
#   -> 3 -> 7 -> 8 -> 9
#                  -> 10
def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    def seek_farthest_node(node):
        max_depth = 0
        farthest_node = node
        seen = set()
        stack = [(node, 0)]
        while stack:
            node, depth = stack.pop()
            seen.add(node)
            if max_depth < depth:
                max_depth = depth
                farthest_node = node
            for next_node in network[node]:
                if next_node in seen:
                    continue
                stack.append((next_node, depth + 1))
        return max_depth, farthest_node

    N = int(input())
    network = defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    _, farthest_node = seek_farthest_node(1)
    max_depth, _ = seek_farthest_node(farthest_node)
    print(max_depth + 1)


if __name__ == "__main__":
    # debug_input()
    main()
