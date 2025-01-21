class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        peak=max(arr)
        for i in range(len(arr)):
            if arr[i]==peak:
                return i