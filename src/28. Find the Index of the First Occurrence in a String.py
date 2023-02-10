class Solution:
    def getNext(self, s: str) -> list:
        next = [0] * len(s)
        j = 0
        next[0] = 0
        for i in range(1, len(next)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        next = self.getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - len(needle) + 1
        return -1


if __name__ == "__main__":
    haystack1 = "aabaabaafa"
    needle1= "aabaaf"
    sol = Solution()
    index = sol.strStr(haystack1, needle1)
    print(index)
