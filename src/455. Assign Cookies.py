class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # appetite
        g.sort()
        # cookies
        s.sort()

        res = 0
        index = len(s) - 1

        for i in range(len(g) - 1, -1, -1):
            # can feed
            # index >= 0 to avoid s[] shorter than g[]
            if index >= 0 and g[i] <= s[index]:
                index -= 1
                res += 1

        return res