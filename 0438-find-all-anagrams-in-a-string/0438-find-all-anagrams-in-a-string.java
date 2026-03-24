class Solution {
    private String sortString(String str) {
        char[] arr = str.toCharArray();
        java.util.Arrays.sort(arr);
        return new String(arr);
    }

    public java.util.List<Integer> findAnagrams(String s, String p) {
        java.util.List<Integer> arr = new java.util.ArrayList<>();
        int start = 0;
        String sortedP = sortString(p);
        String w = "";

        for (int i = 0; i < s.length(); i++) {
            w += s.charAt(i);
            if (w.length() == p.length()) {
                if (sortString(w).equals(sortedP)) {
                    arr.add(start);
                }
                w = w.substring(1);
                start++;
            }
        }
        return arr;
    }
}