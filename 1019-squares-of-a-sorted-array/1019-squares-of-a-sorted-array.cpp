class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n=nums.size();
        vector<int> arr(n);
        for (int i=0;i<n;i++)
        {
            arr[i]=nums[i]*nums[i];
        }
        for(int i=0;i<n-1;i++)
        {
            for (int j=i+1;j<n;j++){
                int temp;
                if (arr[i]>arr[j]){
                    temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
        return arr;
    }
};