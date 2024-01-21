class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = [nums[0]]

        for i_num in nums[1:]:
            current_max.append(max(i_num, current_max[-1] + i_num))

        return max(current_max)
