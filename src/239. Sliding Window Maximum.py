from collections import deque


class PriorityQue:
    def __init__(self):
        self.que = deque()

    def push(self, x):
        while self.que and x > self.que[-1]:
            self.que.pop()
        self.que.append(x)

    def pop(self, x):
        if self.que:
            if x == self.que[0]:
                self.que.popleft()

    def front(self):
        if self.que:
            return self.que[0]


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que = PriorityQue()
        maxList = list()

        for i in range(k):
            que.push(nums[i])
        maxList.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            maxList.append(que.front())

        return maxList


if __name__ == "__main__":
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    nums = [1, -1]
    k = 1
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print("res=", res)