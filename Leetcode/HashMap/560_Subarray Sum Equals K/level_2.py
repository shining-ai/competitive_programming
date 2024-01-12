import collections


def main(nums, k):
    ans = 0
    sum_map = collections.defaultdict(int)
    sum_map[0] = 1
    temp = 0
    for i_num in nums:
        temp += i_num
        ans += sum_map[temp - k]
        sum_map[temp] += 1
    return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 1]
    k = 2
    main(nums, k)
