import collections
import heapq


# O(Nlogk) time, O(N) space
def solve_heap_count(nums, k):
    count = collections.Counter(nums)

    return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solve_heap_count(nums, k))
