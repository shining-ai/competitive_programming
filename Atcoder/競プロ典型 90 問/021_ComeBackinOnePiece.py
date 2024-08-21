import io
import sys

sys.setrecursionlimit(10**7)
_INPUT = """\
4 7
1 2
2 1
2 3
4 3
4 1
1 4
2 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    networks = [set() for _ in range(N)]
    reverse_networks = [set() for _ in range(N)]

    for _ in range(M):
        A, B = map(int, input().split())
        networks[A - 1].add(B - 1)
        reverse_networks[B - 1].add(A - 1)

    # step1: DFSの帰りがけ順で頂点を並べる
    return_node = []
    visited = set()
    for node in range(N):
        if node in visited:
            continue
        stack = [(node, False)]
        while stack:
            current, is_return = stack.pop()
            if is_return:
                return_node.append(current)
                continue
            if current in visited:
                continue
            visited.add(current)
            stack.append((current, True))
            for next_node in networks[current]:
                if next_node in visited:
                    continue
                stack.append((next_node, False))
    # step2: 逆向きのグラフでDFS
    visited = set()
    groups = []
    while return_node:
        node = return_node.pop()
        if node in visited:
            continue
        stack = [node]
        group = [node]
        visited.add(node)
        while stack:
            current = stack.pop()
            for next_node in reverse_networks[current]:
                if next_node in visited:
                    continue
                stack.append(next_node)
                group.append(next_node)
                visited.add(next_node)
        groups.append(group)
    ans = 0
    for group in groups:
        group_num = len(group)
        ans += (group_num * (group_num - 1)) // 2
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
