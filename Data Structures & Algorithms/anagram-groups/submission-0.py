class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            sorted_w = "".join(sorted(word))
            if sorted_w not in word_map:
                word_map[sorted_w] = []
            word_map[sorted_w].append(word)
        return list(word_map.values())