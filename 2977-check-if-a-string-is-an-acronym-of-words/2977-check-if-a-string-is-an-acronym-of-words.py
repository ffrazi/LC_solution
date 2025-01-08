class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        st=""
        for i in words:
            st=st+i[0]
        if st==s:
            return True
        return False