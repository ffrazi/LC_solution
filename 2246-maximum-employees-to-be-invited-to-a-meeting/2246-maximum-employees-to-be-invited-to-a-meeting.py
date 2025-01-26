from collections import deque
class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        inDegree = [0] * n
        for f in favorite:
            inDegree[f] += 1
        queue = deque([i for i in range(n) if inDegree[i] == 0])
        chainLengths = [0] * n
        while queue:
            node = queue.popleft()
            nextNode = favorite[node]
            chainLengths[nextNode] = max(chainLengths[nextNode], chainLengths[node] + 1)
            inDegree[nextNode] -= 1
            if inDegree[nextNode] == 0:
                queue.append(nextNode)
        visited = [False] * n
        maxCycleSize = 0
        twoCycleChains = 0
        for i in range(n):
            if not visited[i] and inDegree[i] > 0:
                cycleSize = 0
                node = i
                while not visited[node]:
                    visited[node] = True
                    node = favorite[node]
                    cycleSize += 1
                if cycleSize == 2:
                    a, b = i, favorite[i]
                    twoCycleChains += 2 + chainLengths[a] + chainLengths[b]
                else:
                    maxCycleSize = max(maxCycleSize, cycleSize)
        return max(maxCycleSize, twoCycleChains)