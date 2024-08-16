import io
import sys
from atcoder.lazysegtree import LazySegTree

_INPUT = """\
3 5
1 2
2 2
2 3
3 3
1 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


class SegmentTree:
    def __init__(self, n):
        self.size = 1
        self.needed_update = []
        while self.size < n:
            self.size *= 2
        self.data = [0] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)

    def update(self, i, val):
        self.data[i] = val
        self.lazy[i] = val  # 子を更新する際に必要な情報を持たせる
        while i > 1:  # 子の更新は必要になるまでしない
            i //= 2
            self.data[i] = max(self.data[i], val)

    def query(self, begin, end, node=1, node_begin=0, node_end=None):
        if node_end is None:
            node_end = self.size
        if node_end <= begin or end <= node_begin:  # 対象区間が被らない
            return 0
        if begin <= node_begin and node_end <= end:  # 対象区間が完全に被る
            self.needed_update.append(node)
            return self.data[node]
        # 一部だけ被る  -> 子ノードに問い合わせ
        node_middle = (node_begin + node_end) // 2
        if self.lazy[node] != 0:  # 保留していた子の更新を行う
            self.update(node * 2, self.lazy[node])
            self.update(node * 2 + 1, self.lazy[node])
            self.lazy[node] = 0
        left_max = self.query(begin, end, node * 2, node_begin, node_middle)
        right_max = self.query(begin, end, node * 2 + 1, node_middle, node_end)
        return max(left_max, right_max)


def main():
    W, N = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    for block in blocks:
        block[0] -= 1
        block[1] -= 1
    all_num = set()
    for block in blocks:
        all_num.add(block[0])
        all_num.add(block[1])
    all_num = sorted(list(all_num))
    blocks_edge_compress = {num: i for i, num in enumerate(all_num)}
    segment_tree = SegmentTree(len(all_num))
    for block in blocks:
        L, R = block
        max_val = segment_tree.query(
            blocks_edge_compress[L], blocks_edge_compress[R] + 1
        )
        for i in segment_tree.needed_update:
            segment_tree.update(i, max_val + 1)
        segment_tree.needed_update = []
        print(max_val + 1)


# SegmentTreeのライブラリを使った解法
# def main():
#     W, N = map(int, input().split())

#     # 初期リスト
#     lst = [0] * W

#     # 区間演算op
#     def op(data1, data2):
#         return max(data1, data2)

#     # opの単位元 op(data1, e) = data1
#     e = -1

#     # lazyをdataに作用させる
#     def mapping(lazy_upper, data_lower):
#         if lazy_upper == -1:
#             return data_lower
#         else:
#             return lazy_upper

#     # lazyをlazyに作用させる
#     def composition(lazy_upper, lazy_lower):
#         if lazy_upper == -1:
#             return lazy_lower
#         else:
#             return lazy_upper

#     # mapping(_id, data_lower) = data_lower
#     _id = -1

#     lazy_segtree = LazySegTree(op, e, mapping, composition, _id, lst)

#     for _ in range(N):
#         l, r = map(int, input().split())
#         l -= 1
#         max_height = lazy_segtree.prod(l, r)
#         lazy_segtree.apply(l, r, max_height + 1)
#         print(max_height + 1)


# 座標圧縮を使った解法
# def main():
#     W, N = map(int, input().split())
#     blocks = [list(map(int, input().split())) for _ in range(N)]
#     for block in blocks:
#         block[0] -= 1
#         block[1] -= 1
#     all_num = set()
#     for block in blocks:
#         all_num.add(block[0])
#         all_num.add(block[1])
#     all_num = sorted(list(all_num))
#     blocks_edge_compress = {num: i for i, num in enumerate(all_num)}

#     heights = [0] * (len(all_num) + 1)
#     for block in blocks:
#         L, R = block
#         max_val = max(heights[blocks_edge_compress[L] : blocks_edge_compress[R] + 1])
#         for i in range(blocks_edge_compress[L], blocks_edge_compress[R] + 1):
#             heights[i] = max_val + 1
#         print(max_val + 1)


# 実直な解法
# def main():
#     W, N = map(int, input().split())
#     heights = [0] * W
#     for _ in range(N):
#         L, R = map(int, input().split())
#         max_val = max(heights[L-1:R])
#         for i in range(L-1, R):
#             heights[i] = max_val + 1
#         print(max_val + 1)


if __name__ == "__main__":
    # debug_input()
    main()
