# import io
# import sys
# from collections import defaultdict

# # import networkx as nx
# import itertools

# _INPUT = """\
# 5
# 4
# 1 2
# 2 3
# 3 4
# 4 5
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 3 1 4 1
# 5 9 2
# 6 5
# 3
# """


# def debug_input():
#     sys.stdin = io.StringIO(_INPUT)


# def main():
#     N = int(input())
#     edges = [i + 1 for i in range(N)]
#     patterns = list(itertools.permutations(edges))
#     M_G = int(input())
#     graph_G = defaultdict(list)
#     for _ in range(M_G):
#         a, b = map(int, input().split())
#         graph_G[a].append(b)
#         graph_G[b].append(a)
#     M_H = int(input())
#     graph_H = defaultdict(list)
#     for _ in range(M_H):
#         c, d = map(int, input().split())
#         graph_H[c].append(d)
#         graph_H[d].append(c)

#     A = []
#     for _ in range(N-1):
#         A.append(list(map(int, input().split())))
#         print(A)

#     min_cost = float("inf")
#     for pattern in patterns:
#         cost = 0
#         for i in range(N):
#             for c in set(graph_G[i + 1]) - set(graph_H[pattern[i]]):
#                 small, big = sorted([i, c])
#                 cost += A[small][big-1]
#             for c in set(graph_H[pattern[i]]) - set(graph_G[i + 1]):
#                 small, big = sorted([i, c])
#                 cost += A[small][big-1]
#         min_cost = min(min_cost, cost)
#     print(min_cost)


# if __name__ == "__main__":
#     debug_input()
#     main()
