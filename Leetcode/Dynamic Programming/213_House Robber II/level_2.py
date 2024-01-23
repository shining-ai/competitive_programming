class Solution:
    def rob(self, nums: List[int]) -> int:
        house_num = len(nums)
        if house_num == 1:
            return nums[0]

        def rob_max(nums):
            house_num = len(nums)
            if house_num == 1:
                return nums[0]

            max_robbed_value = [0] * (house_num + 1)
            max_robbed_value[1] = nums[0]

            for i, i_value in enumerate(nums[1:], start=1):
                max_robbed_value[i+1] = max(
                    max_robbed_value[i],
                    max_robbed_value[i-1] + i_value,
                )

            return max_robbed_value[-1]

        max_value = max(
            rob_max(nums[:-1]),
            rob_max(nums[1:])
        )

        return max_value
