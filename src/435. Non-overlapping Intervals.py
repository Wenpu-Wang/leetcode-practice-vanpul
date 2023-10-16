class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        overlap = 1
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            # 算出非交叉区间（不能直接射箭穿爆）的个数，只需要修改<变成<=
            if intervals[i - 1][1] <= intervals[i][0]:
                overlap += 1
            else:
                intervals[i][1] = min(intervals[i - 1][1], intervals[i][1])

        return len(intervals) - overlap
