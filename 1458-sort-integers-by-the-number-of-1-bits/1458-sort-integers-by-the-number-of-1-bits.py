from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i].bit_count(), arr[i]) > (arr[j].bit_count(), arr[j]):  
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
