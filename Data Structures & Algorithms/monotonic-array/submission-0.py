class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc = True
            elif nums[i] > nums[i + 1]:
                dec = True
        return not (inc and dec)