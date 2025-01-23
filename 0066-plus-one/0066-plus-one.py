class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=0
        result=[]
        for i in digits:
            i=int(i)
            x=x*10+i
        x+=1
        x=str(x)
        for i in x:
            result.append(int(i))
        return result 