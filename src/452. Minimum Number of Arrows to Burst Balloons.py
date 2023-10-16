class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        arrow = 1
        if len(points) == 1:
            return arrow
        points.sort(key=lambda x: x[0], reverse=False)
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:
                arrow += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])
        return arrow
