class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        s = []
        res = [0] * len(temp)
        for i in range(len(temp)-1, -1, -1):
            while s and temp[s[-1]] <= temp[i]:
                s.pop()
            res[i] = 0 if len(s) == 0 else s[-1] - i
            s.append(i)
        return res