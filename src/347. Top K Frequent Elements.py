import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        di = dict()
        for num in nums:
            di[num] = di.get(num, 0) + 1
        que = list()
        for key, value in di.items():
            heapq.heappush(que, (value, key))
            if len(que) > k:
                heapq.heappop(que)
        res = list()
        for _ in range(len(que)):
            res.append(heapq.heappop(que)[1])
        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    que = sol.topKFrequent(nums, k)
    print(que)
