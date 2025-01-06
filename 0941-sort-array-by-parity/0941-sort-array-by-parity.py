class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        oa=[]
        ea=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                ea.append(nums[i])
            else:
                oa.append(nums[i])
        return ea+oa