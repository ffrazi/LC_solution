class Solution:
    def trap(self, height):
        maxwater = 0
        n = len(height)
        left, right = 0, n - 1
        leftmax, rightmax = height[0], height[n - 1]
        
        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            
            if leftmax < rightmax:
                maxwater += leftmax - height[left]
                left += 1
            else:
                maxwater += rightmax - height[right]
                right -= 1
        
        return maxwater
