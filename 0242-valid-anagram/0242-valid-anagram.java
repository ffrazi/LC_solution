import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> maps = new HashMap<>();
        HashMap<Character, Integer> mapt = new HashMap<>();

        for (char c : s.toCharArray()) {
            maps.put(c, maps.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            mapt.put(c, mapt.getOrDefault(c, 0) + 1);
        }

        for (char key : maps.keySet()) {
            if (!maps.get(key).equals(mapt.getOrDefault(key, 0))) {
                return false;
            }
        }

        return true;
    }
}
