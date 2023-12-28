import io
import sys
from collections import deque


def debug_input():
    _INPUT = """\
4 2
0 1 1 0
1 2 3
2 3 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    actions = [
        list(map(lambda x: int(x) - 1, input().split())) for i in range(M)
    ]  # ここでは X[i], Y[i], Z[i] を 0-indexed に変換して受け取る

    def get_next(pos, x, y, z):
        # pos の 2 進法表記を使って、頂点 pos が表すランプの状態 state を計算
        # （pos の 2^i の位は (pos // (2 ** i)) % 2 で計算できる → 1.4 節を参照）
        state = [(pos // (2**i)) % 2 for i in range(N)]
        # ランプ x, y, z を反転
        state[x] = 1 - state[x]
        state[y] = 1 - state[y]
        state[z] = 1 - state[z]
        # ランプの状態 state を指す頂点の番号を計算
        # （2 進法を 10 進法に変換する方法は 1.4 節を参照）
        ret = 0
        for i in range(N):
            if state[i] == 1:
                ret += 2**i
        return ret

    # グラフに辺を追加
    net = [list() for i in range(2**N)]
    for i in range(2**N):
        for x, y, z in actions:
            nextstate = get_next(i, x, y, z)
            net[i].append(nextstate)

    start = 0
    for i in range(N):
        if A[i] == 1:
            start += 2**i
    goal = 2**N - 1

    dist = [-1] * (2**N)
    dist[start] = 0
    Q = deque()
    Q.append(start)

    # 幅優先探索
    while len(Q) >= 1:
        pos = Q.popleft()  # キュー Q の先頭要素を取り除き、その値を pos に代入する
        for nex in net[pos]:
            if dist[nex] == -1:
                dist[nex] = dist[pos] + 1
                Q.append(nex)

    # 答えを出力
    print(dist[goal])


if __name__ == "__main__":
    # debug_input()
    main()
