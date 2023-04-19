class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        cur_sum = 0
        start = 0
        total_sum = 0

        rest = [0] * len(gas)
        for i in range(len(gas)):
            rest[i] = gas[i] - cost[i]
            cur_sum += rest[i]
            total_sum += rest[i]

            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        if total_sum < 0:
            return -1
        return start
