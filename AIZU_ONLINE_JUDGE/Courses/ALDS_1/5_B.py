import io
import sys


def debug_input():
    _INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    A_langth = int(input())
    A = list(map(int, input().split()))
    compare_num = 0

    def merge(left, mid, right):
        left_list = A[left : mid + 1]
        right_list = A[mid + 1 : right + 1]
        left_list.append(float("inf"))
        right_list.append(float("inf"))
        left_index = 0
        right_index = 0
        for i in range(left, right + 1):
            if left_list[left_index] < right_list[right_index]:
                A[i] = left_list[left_index]
                left_index += 1
            else:
                A[i] = right_list[right_index]
                right_index += 1

    def merge_sort(left, right):
        nonlocal compare_num
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)
        compare_num += right - left + 1

    merge_sort(0, A_langth - 1)
    print(" ".join(map(str, A)))
    print(compare_num)


if __name__ == "__main__":
    # debug_input()
    main()
