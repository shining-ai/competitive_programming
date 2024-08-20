import io
import sys

# from atcoder.segtree import SegTree

_INPUT = """\
100 4
13 15 31415
12 13 92653
29 33 58979
95 98 32384

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


# rootのindexは1
class SegmentTree:
    def __init__(self, nums):
        self.size = 1 << (len(nums) - 1).bit_length()
        self.tree = [-1] * (self.size * 2)
        # 葉ノードに値をセット
        for i, num in enumerate(nums):
            self.tree[self.size + i] = num
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, left, right):
        left += self.size
        right += self.size
        res = -1
        while left < right:
            if left & 1:
                res = max(res, self.tree[left])
                left += 1
            if right & 1:
                res = max(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def main():
    W, N = map(int, input().split())
    max_val = [[-1] * (W + 1) for _ in range(N + 1)]
    max_val[0][0] = 0
    rmq = SegmentTree(max_val[0])
    # rmq = SegTree(max, -1, max_val[0])
    for i in range(1, N + 1):
        L, R, V = map(int, input().split())
        for spice in range(W + 1):
            max_val[i][spice] = max_val[i - 1][spice]
            right = spice - L + 1
            if right <= 0:
                continue
            left = max(0, spice - R)
            add_val = rmq.query(left, right) + V
            # add_val = rmq.prod(left, right) + V
            if add_val < V:
                continue
            max_val[i][spice] = max(max_val[i][spice], add_val)
        rmq = SegmentTree(max_val[i])
        # rmq = SegTree(max, -1, max_val[i])

    ans = -1
    # print(max_val)
    for i in range(N + 1):
        ans = max(ans, max_val[i][W])
    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
