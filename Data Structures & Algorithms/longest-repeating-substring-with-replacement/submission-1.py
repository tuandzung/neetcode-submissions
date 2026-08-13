class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ctr = Counter()
        j = 0
        res = 0
        for i in range(len(s)):
            ctr[s[i]] += 1
            most_common_cnt = ctr.most_common()[0][1]
            cur_len = i - j + 1
            if cur_len - most_common_cnt > k:
                ctr[s[j]] -= 1
                j += 1
                continue
            res = max(res, cur_len)
        return res
        