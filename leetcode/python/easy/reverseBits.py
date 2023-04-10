'''
190. Reverse Bits

Difficulty: Easy

Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        temp = 0
        
        for i in range(32):
            temp = (temp<<1) + (n&1)
            n >>= 1

        return temp