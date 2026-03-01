class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        up = 0
        down = 0
        prev = arr[0]
        res = 0

        for x in arr:
            if x > prev:
                if down > 0:
                    up = 0
                    down = 0
                
                up += 1
            elif x < prev:
                if up:
                    down += 1
                    res = max(res, up + down + 1)
            else:
                up = 0
                down = 0
            prev = x

        return res