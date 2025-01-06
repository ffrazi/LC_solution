class Solution {
    public int[] sortArrayByParity(int[] nums) {
        List<Integer> ea= new ArrayList<>();
        List<Integer> oa= new ArrayList<>();
        for (int i=0;i<nums.length;i++){
            if (nums[i]%2==0){
                ea.add(nums[i]);
            }
            else{
                oa.add(nums[i]);
            }
        }
        ea.addAll(oa);
        int [] result = new int[ea.size()];
        for (int i=0;i<ea.size();i++){
            result[i]=ea.get(i);
        }
        return result;
    }
}