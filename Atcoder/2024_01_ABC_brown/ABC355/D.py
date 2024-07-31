import io
import sys
from sortedcontainers import SortedList


def debug_input():
    _INPUT = """\
3
3 4
2 5
1 6
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    N = int(input())
    jobs = list(tuple(map(int, input().split())) for _ in range(N))
    jobs.sort(key=lambda x: x[0])
    sorted_list = SortedList()
    count = 0
    for i in range(len(jobs) - 1, -1, -1):
        num = sorted_list.bisect_right(jobs[i][1])
        count += num
        sorted_list.add(jobs[i][0])
    print(count)


if __name__ == "__main__":
    # debug_input()
    main()
