class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ctr = Counter()
        j = 0
        res = 0
        max_freq = 0
        for i in range(len(s)):
            ctr[s[i]] += 1
            max_freq = max(max_freq, ctr[s[i]])
            cur_len = i - j + 1
            if cur_len - max_freq > k:
                ctr[s[j]] -= 1
                j += 1
            else:
                res = max(res, cur_len)
        return res
