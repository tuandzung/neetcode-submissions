class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        MAX_NUMS = 10**9
        mapping = {}
        for n in nums:
            if n not in mapping:
                mapping[n] = 0
            mapping[n] += 1
            if mapping[n] > 1:
                return True
        return False