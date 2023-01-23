'''
205. Isomorphic Strings

Difficulty: Easy

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
'''
#Needed LeetCode Help
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.transform(s) == self.transform(t)
    
    def transform(self, s: str) -> str:    
        mapp = {}
        new = []
        
        for i, c in enumerate(s):
            if c not in mapp:
                mapp[c] = i
            new.append(str(mapp[c]))
            
        return " ".join(new)
