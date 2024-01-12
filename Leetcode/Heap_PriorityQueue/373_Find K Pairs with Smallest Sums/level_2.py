from heapq import heapify, heappop, heappush


def main(nums1, nums2, k):
    heap = []

    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heappush(heap, [nums1[i] + nums2[j], i, j])

    push(0, 0)
    ans = []

    for _ in range(k):
        _, i, j = heappop(heap)
        ans.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)

    return ans


if __name__ == "__main__":
    nums1 = [-10, -4, 0, 0, 6]
    nums2 = [3, 5, 6, 7, 8, 100]
    k = 30

    print(main(nums1, nums2, k))
