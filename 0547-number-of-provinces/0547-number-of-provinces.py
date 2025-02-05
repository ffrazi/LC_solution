class Solution:
    def dfs(self, N, city, isConnected, visited):
        visited[city] = True  # Mark city as visited
        for othCity in range(N):
            if not visited[othCity] and isConnected[city][othCity] == 1:
                self.dfs(N, othCity, isConnected, visited)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        N = len(isConnected)
        province = 0
        visited = [False] * N  # Boolean array to track visited cities

        for city in range(N):
            if not visited[city]:  # If the city is not visited, start DFS
                province += 1
                self.dfs(N, city, isConnected, visited)

        return province
