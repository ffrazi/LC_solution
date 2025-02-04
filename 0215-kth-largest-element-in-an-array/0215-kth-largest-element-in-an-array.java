class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int num:nums){
            maxHeap.add(num);
        }
        for(int ctr=1;ctr<k;ctr++)
        {
            maxHeap.poll();
        }
        return maxHeap.poll();
    }
}