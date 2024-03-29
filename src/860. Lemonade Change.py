class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            if bill == 20:
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
    