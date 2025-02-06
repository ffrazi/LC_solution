class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        leftmax=height[0]
        sum=0
        j=len(height)-1
        rightmax=height[j]
        while i<j:
            if leftmax <= rightmax:
                sum+=leftmax-height[i]
                i+=1
                leftmax=max(leftmax,height[i])
            else:
                sum+=rightmax-height[j]
                j-=1
                rightmax=max(rightmax,height[j])
        return sum