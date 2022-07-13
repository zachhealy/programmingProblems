#Difficulty: Medium

#7. Reverse Integer

#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
#signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

#Example 1:
#Input: x = 123
#Output: 321

#Example 2:
#Input: x = -123
#Output: -321

#Example 3:
#Input: x = 120
#Output: 21

#Constraints:
#-2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        newNum = ""
        
        for i in range(len(num) - 1, -1, -1):
            if num[i] == '-':
                newNum = '-' + newNum
            else:
                newNum = newNum + num[i]
                
        newNum = int(newNum)
        if newNum > 2147483647 or newNum < -2147483647:
            return 0
        else:
            return newNum
