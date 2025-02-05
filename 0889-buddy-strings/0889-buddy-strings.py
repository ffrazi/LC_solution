class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count=[]
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        for i in range(len(s)):
            if s[i]!=goal[i]:
                count.append(i)
        if len(count)==0:
            return True
        return len(count)==2 and s[count[0]]==goal[count[1]] and s[count[1]]==goal[count[0]]