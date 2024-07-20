import io
import sys
import collections

_INPUT = """\
6
-87 12
-60 -54
2 38
-76 6
87 96
-17 38

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    min_sum = 0
    max_sum = 0
    L_list = []
    R_list = []
    for i in range(N):
        L, R = map(int, input().split())
        min_sum += L
        max_sum += R
        L_list.append(L)
        R_list.append(R)

    if not (min_sum <= 0 <= max_sum):
        print("No")
        return

    X_list = []
    L_queue = collections.deque(L_list)

    for i in range(N):
        if min_sum == 0:
            break
        low = L_queue.popleft()
        high = R_list[i]
        if high - low > -min_sum:
            X_list.append(low - min_sum)
            break
        X_list.append(high)
        min_sum += high - low

    X_list += list(L_queue)
    print("Yes")
    for X in X_list:
        print(X, end=" ")


if __name__ == "__main__":
    # debug_input()
    main()
