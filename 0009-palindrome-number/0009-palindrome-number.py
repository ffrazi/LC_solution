class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        rev=0
        while x>0:
            n=x%10
            rev= rev*10+n
            x=x//10
        return rev == original