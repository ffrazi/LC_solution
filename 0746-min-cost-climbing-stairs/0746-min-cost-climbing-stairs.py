class Solution:
    def __init__(self):
        self.dp = {}

    def minCostClimbingStairs(self, cost):
        n = len(cost)
        return min(self.solve(n - 1, cost), self.solve(n - 2, cost))

    def solve(self, i, cost):
        if i <= 1:
            return cost[i]

        if i in self.dp:
            return self.dp[i]

        self.dp[i] = cost[i] + min(self.solve(i - 1, cost), self.solve(i - 2, cost))
        return self.dp[i]
