class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # if len(nums) == 1:
        #     return True
        i = 0
        cover = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            i += 1
            if cover >= len(nums) - 1: return True
        return False
