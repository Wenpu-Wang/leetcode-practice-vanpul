class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # print(people)
        que = list()
        for p in people:
            que.insert(p[1], p)
        return que
