class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord("a")] = i
        left, right = 0, 0

        res = list()
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord("a")])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res

