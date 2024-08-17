import io
import sys
from collections import Counter, defaultdict

_INPUT = """\
4 3
2 1 4 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))
    # ruiseki = [0] * N
    # ruiseki[0] = A[0] % M
    # for i in range(1, N):
    #     ruiseki[i] = (ruiseki[i - 1] + A[i]) % M
    # ruiseki_count = Counter(ruiseki)

    # ans = 0
    # current = 0
    # for i in range(N):
    #     ans += ruiseki_count[current]
    #     ruiseki_count[ruiseki[i]] -= 1
    #     new_ruiseki = (ruiseki[-1] + A[i]) % M
    #     ruiseki.append(new_ruiseki)
    #     ruiseki_count[new_ruiseki] += 1
    #     current = ruiseki[i]
    # print(ans)


if __name__ == "__main__":
    debug_input()
    main()
