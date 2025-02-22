import io
import sys


def debug_input():
    _INPUT = """\
3
3 1 2
    """

    sys.stdin = io.StringIO(_INPUT)


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    def merge(left, mid, right):
        count = 0
        left_list = nums[left: mid + 1]
        right_list = nums[mid + 1: right + 1]
        left_list.append(float("inf"))
        right_list.append(float("inf"))
        left_index = 0
        right_index = 0
        for i in range(left, right + 1):
            if left_list[left_index] < right_list[right_index]:
                nums[i] = left_list[left_index]
                left_index += 1
            else:
                nums[i] = right_list[right_index]
                count += (mid - left_index + 1 - left)
                right_index += 1
        return count

    def merge_sort(left, right):
        count = 0
        if left >= right:
            return 0
        mid = (left + right) // 2
        count += merge_sort(left, mid)
        count += merge_sort(mid + 1, right)
        count += merge(left, mid, right)
        return count
    print(merge_sort(0, n - 1))


if __name__ == "__main__":
    # debug_input()
    main()
