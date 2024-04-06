import collections
import heapq
import io
import sys

# 単純なBFSで解くと、O(HW)^2となりタイムアウトする
# heapqでコストの大きい順に取り出すと高速化された。


def debug_input():
    _INPUT = """\
4 5
..#..
.S##.
.##T.
.....
3
3 1 5
1 2 3
2 2 1

    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    medicine = collections.defaultdict(list)
    for i in range(N):
        R, C, E = map(int, input().split())
        medicine[(R - 1, C - 1)] = E
    seen = collections.defaultdict(lambda: -1)

    for h in range(H):
        for w in range(W):
            if field[h][w] == "S":
                start = (h, w)

    heap = []
    heapq.heappush(heap, (0, start))

    def add_stack(pos_h, pos_w, energy):
        if not (0 <= pos_h < H and 0 <= pos_w < W):
            return
        if seen[(pos_h, pos_w)] >= energy:
            return
        seen[(pos_h, pos_w)] = energy
        if field[pos_h][pos_w] != "#":
            heapq.heappush(heap, (-energy, (pos_h, pos_w)))

    while heap:
        energy, (pos_h, pos_w) = heapq.heappop(heap)
        energy = -energy
        seen[(pos_h, pos_w)] = energy
        if (pos_h, pos_w) in medicine:
            energy = max(energy, medicine[(pos_h, pos_w)])
        if field[pos_h][pos_w] == "T":
            print("Yes")
            return
        if energy != 0:
            add_stack(pos_h + 1, pos_w, energy - 1)
            add_stack(pos_h - 1, pos_w, energy - 1)
            add_stack(pos_h, pos_w + 1, energy - 1)
            add_stack(pos_h, pos_w - 1, energy - 1)
    print("No")


if __name__ == "__main__":
    # debug_input()
    main()
