class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        nums = sorted(set(nums))
        res = 0
        for i in range(len(nums)):
            j = i
            if nums[i] - 1 not in uniq_nums:
                while nums[j] + 1 in uniq_nums:
                    j += 1
                res = max(res, j - i + 1)
        return res