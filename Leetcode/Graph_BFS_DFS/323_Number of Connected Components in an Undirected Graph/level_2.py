def main(n, edges):
    all_nodes = set(range(n))
    seen = set()
    non_seen = all_nodes - seen
    net = [set() for _ in range(n)]
    ans = 0

    for i_edge in edges:
        net[i_edge[0]].add(i_edge[1])
        net[i_edge[1]].add(i_edge[0])

    def dfs(i_node):
        seen.add(i_node)
        for i_child in net[i_node]:
            if i_child not in seen:
                dfs(i_child)

    while non_seen:
        dfs(non_seen.pop())
        ans += 1
        non_seen = all_nodes - seen

    return ans


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(main(n, edges))
