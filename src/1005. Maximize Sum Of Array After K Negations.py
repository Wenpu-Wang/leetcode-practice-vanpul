class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1

        nums[-1] *= (-1) ** k
        return sum(nums)
