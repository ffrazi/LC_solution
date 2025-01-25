class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n=len(nums)
        arr=[]
        for i in range(n):
            arr.append([nums[i],i])
        arr.sort()
        i=0
        j=1
        while (i<n and j<n):
            while (j<n and abs(arr[j][0]-arr[j-1][0])<=limit):
                j+=1
            group=[]
            indices=[]
            for k in range(i,j):
                group.append(arr[k][0])
                indices.append(arr[k][1])
            i=j
            j+=1
            group.sort()
            indices.sort()
            for m in range(len(group)):
                nums[indices[m]]=group[m]
        return nums