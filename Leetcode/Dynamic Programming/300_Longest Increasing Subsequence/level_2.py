class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for i_num in nums:
            combo = bisect.bisect_left(sub, i_num)

            if combo >= len(sub):
                sub.append(i_num)

            if sub[combo] > i_num:
                sub[combo] = i_num

        return len(sub)
