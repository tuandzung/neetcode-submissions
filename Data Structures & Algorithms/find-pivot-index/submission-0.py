class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = suffix[i] + nums[i]
        for i in range(len(nums)):
            if suffix[i] == prefix[i]:
                return i
        return -1