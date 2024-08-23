import io
import sys

sys.setrecursionlimit(10**9)
_INPUT = """\
2
1 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# 最短ルートは、全てのノードの子ノードの数から算出できる
def main():
    N = int(input())
    network = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        network[a - 1].append(b - 1)
        network[b - 1].append(a - 1)
    visited = set()
    visited.add(0)
    child_nums = [1] * N

    def dfs(child_num):
        for child in network[child_num]:
            if child in visited:
                continue
            visited.add(child)
            dfs(child)
            child_nums[child_num] += child_nums[child]

    dfs(0)
    ans = 0
    for child_num in child_nums:
        ans += child_num * (N - child_num)
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
