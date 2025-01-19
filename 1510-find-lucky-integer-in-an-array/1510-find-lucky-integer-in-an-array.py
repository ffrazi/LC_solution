class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=list(set(arr))
        c_arr=[]
        for i in l:
            c=arr.count(i)
            c_arr.append(c)
        value=0
        for i in range(len(l)):
            if c_arr[i]==l[i]:
                if l[i]>value:
                    value=l[i]
        if value==0:
            return -1
        return value