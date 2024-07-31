import io
import sys
from collections import deque


def debug_input():
    _INPUT = """\
4 1
2 3 1 4


    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = float("inf")
    l = []
    for i, p in enumerate(P):
        l.append((i + 1, p))
    l = sorted(l, key=lambda x: x[1])
    needed_data = []
    for i in l:
        needed_data.append(i[0])

    min_index = [0] * (N)  # [i-K+1, i]の区間での最小値のindex
    min_index_deque = deque(range(K))
    max_index = [0] * (N)  # [i-K+1, i]の区間での最大値のindex
    max_index_deque = deque(range(K))

    for i in range(N):
        if min_index_deque and min_index_deque[0] < i - K + 1:
            min_index_deque.popleft()
        while min_index_deque and needed_data[min_index_deque[-1]] >= needed_data[i]:
            min_index_deque.pop()
        min_index_deque.append(i)
        min_index[i] = min_index_deque[0]

        if max_index_deque and max_index_deque[0] < i - K + 1:
            max_index_deque.popleft()
        while max_index_deque and needed_data[max_index_deque[-1]] <= needed_data[i]:
            max_index_deque.pop()
        max_index_deque.append(i)
        max_index[i] = max_index_deque[0]

    # print(needed_data)
    # print(min_index)
    # print(max_index)
    for i in range(K-1, N):
        # print(ans, needed_data[max_index[i]], needed_data[min_index[i]])
        ans = min(
            ans, needed_data[max_index[i]] - needed_data[min_index[i]]
        )

    print(ans)


if __name__ == "__main__":
    # debug_input()
    main()
