class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        return list(dict(sorted(counts.items(), key=lambda item: (-item[1], item[0]))).keys())[:k]
        