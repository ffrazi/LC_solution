class Solution {
    public int maxProduct(int[] nums) {
        int pre=1,suf=1;
        int res = Integer.MIN_VALUE;
        int n=nums.length;
        
        for (int i=0;i<n;i++){
            pre*=nums[i];
            suf*=nums[n-i-1];
            res=Math.max(res,Math.max(pre,suf));
            if (pre==0){
                pre=1;
            }
            if(suf==0){
                suf=1;
            }
        }
        return res;
    }
}