from itertools import combinations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        allseq=set()
        def backtracking(word,visited):
            for i in range(len(tiles)):
                if visited[i]:
                    continue
                charseq=word+tiles[i]
                visited[i]=True
                allseq.add(charseq)
                backtracking(charseq,visited)
                visited[i]=False
        backtracking("",[False]*len(tiles))
        return len(allseq)