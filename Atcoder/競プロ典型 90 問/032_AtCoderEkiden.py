import io
import sys
import itertools

_INPUT = """\
3
1 10 100
10 1 100
100 10 1
1
1 2
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    men = list(range(N))
    M = int(input())
    bad_relations = [set() for _ in range(N)]
    for i in range(M):
        x, y = map(int, input().split())
        bad_relations[x - 1].add(y - 1)
        bad_relations[y - 1].add(x - 1)
    min_time = float("inf")
    candidates = list(itertools.permutations(men))
    for candidate in candidates:
        time = 0
        prev = -1
        for course, man in enumerate(candidate):
            if prev in bad_relations[man]:
                break
            prev = man
            time += A[man][course]
        else:
            min_time = min(min_time, time)
    if min_time == float("inf"):
        print(-1)
    else:
        print(min_time)


if __name__ == "__main__":
    debug_input()
    main()
