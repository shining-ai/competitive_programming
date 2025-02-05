import io
import sys


def debug_input():
    _INPUT = """\
5
1 5 7 10 21
4
2 4 17 8
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A_langth = int(input())
    A = list(map(int, input().split()))
    q_num = int(input())
    q = list(map(int, input().split()))
    sum_list = set()

    def helper(current, index):
        sum_list.add(current)
        for i in range(index, A_langth):
            current += A[i]
            helper(current, i + 1)
            current -= A[i]

    helper(0, 0)
    for target in q:
        if target in sum_list:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    # debug_input()
    main()
