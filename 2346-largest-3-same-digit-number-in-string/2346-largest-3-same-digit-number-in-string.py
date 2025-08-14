class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr=0
        s=[]
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2] and int(num[i])>=curr:
                s.append(int(num[i:i+3]))
        if not s:
            return ""
        return str(max(s)).zfill(3)