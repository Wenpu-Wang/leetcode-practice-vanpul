class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        cur_distance = 0
        next_distance = 0
        res = 0
        # for i in range(len(nums) - 1):
        for i in range(len(nums)):
            # update every step
            next_distance = max(next_distance, nums[i] + i)
            if i == cur_distance:
                res += 1
                if next_distance >= len(nums) - 1:
                    break
                cur_distance = next_distance
        return res

class Solution1:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        cur_distance = 0
        next_distance = 0
        res = 0
        for i in range(len(nums) - 1):
            # update every step
            next_distance = max(next_distance, nums[i] + i)
            if i == cur_distance:
                res += 1
                cur_distance = next_distance
        return res