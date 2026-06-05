class Solution {
    public int maximumCount(int[] nums) {
        int poscon=0;
        int negcon=0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]<0){
                negcon++;
            }
            else if(nums[i]>0){
                poscon++;
            }
        }
        return Math.max(poscon,negcon);
    }
}