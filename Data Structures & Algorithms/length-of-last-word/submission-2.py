class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        j = -1
        s = s.strip()
        for i in range(len(s)):
            if s[i] == ' ':
                j = i
            res = i - j
        return res