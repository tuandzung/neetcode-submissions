class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
            if cnt[n] > threshold:
                return n