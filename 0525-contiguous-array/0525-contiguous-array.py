class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen=0
        values={0:-1}
        counter=0
        for i,num in enumerate(nums):
            counter+=1 if num==0 else -1
            if counter in values:
                maxlen=max(maxlen,i-values[counter])
            else:
                values[counter]=i
        return maxlen