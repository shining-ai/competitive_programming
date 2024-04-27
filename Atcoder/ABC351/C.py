import collections
import io
import sys


def debug_input():
    _INPUT = """\
7
2 1 1 3 5 3 3
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    queue = collections.deque([A[0]])

    for a in A[1:]:
        current = a
        while queue and queue[-1] == current:
            queue.pop()
            current += 1
        queue.append(current)

    print(len(queue))


if __name__ == "__main__":
    # debug_input()
    main()
