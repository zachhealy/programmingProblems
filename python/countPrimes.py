''''
204. Count Primes

Difficulty: Medium

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106

''''


#WORK IN PROGRESS
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        lst = []
        for i in range(2, n):
            for j in range(2, int(i/2) + 1):
                if (i % j) == 0:
                    break    
            else:
                lst.append(i)
        
        return len(lst)
