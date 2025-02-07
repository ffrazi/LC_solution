class Solution {
    public boolean canJump(int[] nums) {
        int N=nums.length;
        int maxReach=0,reach=0;
        for(int ctr=0; ctr<N-1;ctr++){
            if(ctr>maxReach){
                return false;
            }
            reach=nums[ctr]+ctr;
            maxReach=Math.max(reach,maxReach);
        }
        if(maxReach>=N-1){
            return true;
        }
        else{
            return false;
        }
    }
}