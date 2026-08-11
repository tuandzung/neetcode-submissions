class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, n in enumerate(nums):
            if target - n in ind:
                return [ind[target - n] + 1, i + 1]
            ind[n] = i
        