class Solution {
    public int findMaxLength(int[] nums) {
            Map<Integer,Integer> map=new HashMap<>();
            map.put(0,-1);
            int maxLen=0;
            int counter=0;
            int n=nums.length;
            for(int index=0;index<n;index++){
                if(nums[index]==1){
                    counter++;
                }
                else{
                    counter--;
                }
                if(map.containsKey(counter)){
                    int currLen=index-map.get(counter);
                    maxLen=Math.max(maxLen,currLen);
                }
                else map.put(counter,index);
                }
            return maxLen;
    }
}