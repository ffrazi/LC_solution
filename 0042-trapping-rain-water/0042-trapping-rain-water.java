class Solution {
    public int trap(int[] height) {
        int maxwater=0,n=height.length;
        int left=0,right=n-1,leftmax=height[0],rightmax=height[n-1];
        while(left<right){
            leftmax=Math.max(leftmax,height[left]);
            rightmax=Math.max(rightmax,height[right]);
            if(leftmax<rightmax){
                maxwater+=leftmax-height[left++];
            }
            else{
                maxwater+=rightmax-height[right--];
            }
        }
        return maxwater;
    }
} 