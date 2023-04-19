class Solution:
    def candy(self, ratings: list[int]) -> int:
        candy_vec = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_vec[i] = candy_vec[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_vec[i] = max(candy_vec[i], candy_vec[i+1] + 1)
        return sum(candy_vec)