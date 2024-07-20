import io
import sys
import collections
import math
import itertools

_INPUT = """\
5 3
zabyx

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N, K = map(int, input().split())
    S = input()
    freqs = collections.Counter(S)
    S = [c for c in S]

    all_paterns = set()
    for f in freqs.values():
        if f != 1:
            break
    else:
        all_num = 1
        n = N
        for freq in freqs.values():
            all_num *= math.comb(n, freq)
            n -= freq
        print(all_num)
        return

    for pair in itertools.permutations(S, N):
        all_paterns.add(pair)

    ans = 0
    for pattern in all_paterns:
        for i in range(N - K + 1):
            if pattern[i : i + K] == pattern[i : i + K][::-1]:
                break
        else:
            ans += 1
    print(ans)




if __name__ == "__main__":
    # debug_input()
    main()
