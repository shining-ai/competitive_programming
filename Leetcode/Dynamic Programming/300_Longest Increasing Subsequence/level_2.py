class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [-float("inf")]
        max_combo = 0

        for i_num in nums:
            combo = bisect.bisect_left(sub, i_num)

            if combo > max_combo:
                sub.append(i_num)
                max_combo = combo

            if sub[combo] > i_num:
                sub[combo] = i_num

        return max_combo
