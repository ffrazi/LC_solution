class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff]+1,i+1]
            hashmap[n]=i