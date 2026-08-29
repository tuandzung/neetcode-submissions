class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l = 0
        res = 0
        sub_sum = 0
        for r in range(len(nums)):
            if nums[r] <= nums[r - 1]:
                l = r
                sub_sum = 0
            sub_sum += nums[r]
            res = max(res, sub_sum)
        return res