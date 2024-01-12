def solve_1(n, edges):
    all_nodes = set(range(n))
    seen = set()
    non_seen = all_nodes - seen
    net = [set() for _ in range(n)]
    ans = 0

    for i_edge in edges:
        net[i_edge[0]].add(i_edge[1])
        net[i_edge[1]].add(i_edge[0])

    while non_seen:
        stack = [non_seen.pop()]
        seen.add(stack[0])
        while stack:
            i_node = stack.pop()
            for i_child in net[i_node]:
                if i_child not in seen:
                    stack.append(i_child)
                    seen.add(i_child)

        non_seen = all_nodes - seen
        ans += 1

    return ans


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(solve_1(n, edges))
