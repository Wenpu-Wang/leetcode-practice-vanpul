class Solution:
    def getNext(self, s: str) -> list:
        next = [0] * len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        next = self.getNext(s)
        print(s)
        print(next)
        # if the string's length is one, or there is no equal prefix and suffix
        # then: next[-1] == 0
        if next[-1] != 0 and len(next) % (len(next) - next[-1]) == 0:
            return True
        return False

