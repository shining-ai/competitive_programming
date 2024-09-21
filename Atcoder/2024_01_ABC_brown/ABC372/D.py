import io
import sys
from heapq import heappop, heappush

_INPUT = """\
10
1 9 6 5 2 7 10 4 8 3

"""


def debug_input():
    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    max_height = 0
    ans = [0]
    min_heap = []
    for i in reversed(H):
        if max_height < i:
            count = 1
            min_heap = []
            ans.append(count)
            max_height = i
            heappush(min_heap, i)
            continue
        count += 1
        while min_heap and min_heap[0] < i:
            heappop(min_heap)
            count -= 1
        ans.append(count)
        heappush(min_heap, i)
    ans.pop()
    print(*reversed(ans))



if __name__ == "__main__":
    # debug_input()
    main()
