class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        for c in t:
            char_count[c] = char_count.get(c, 0) - 1
        return all(v == 0 for v in char_count.values())
        