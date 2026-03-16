class Solution {
    public String reverseStr(String s, int k) {
        char[] st = s.toCharArray();
        int n=st.length-1;
        for(int i=0;i<n;i+=2*k){
            int left=i;
            int right= Math.min(i+k-1,n);

            while(left<right){
                char temp = st[left];
                st[left]=st[right];
                st[right]=temp;
                left++;
                right--;
            }
        }
        return new String(st);
    }
}