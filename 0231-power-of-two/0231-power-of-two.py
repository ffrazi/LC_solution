class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        setbits = 0
        while n:
            setbits += n & 1
            n >>= 1
        return setbits == 1
