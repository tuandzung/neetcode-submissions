class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min([Counter(text)[k] // v for k, v in Counter("balloon").items()])