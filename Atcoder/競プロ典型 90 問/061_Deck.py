import io
import sys
from collections import deque

_INPUT = """\
6
1 2
1 1
2 3
3 1
3 2
3 3
"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    Q = int(input())
    queue = deque()
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            queue.append(query[1])
        elif query[0] == 2:
            queue.appendleft(query[1])
        else:
            print(queue[-query[1]])


if __name__ == "__main__":
    # debug_input()
    main()
