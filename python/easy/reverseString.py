'''
344. Reverse String

Difficulty: Easy

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:
1 <= s.length <= 10^5
s[i] is a printable ascii character.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev = s.copy()
        del s [:]

        i = len(rev) - 1

        while i >= 0:
            s.append(rev[i])
            i -= 1