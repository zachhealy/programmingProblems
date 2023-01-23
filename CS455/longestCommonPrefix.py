'''
14. Longest Common Prefix

Difficulty: Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return ""
        
        for i in range(len(strs[0])):
            pre = strs[0][i]

            for j in strs:
                try:
                    if j[i] != pre:
                        return strs[0][:i]
                except:
                    return strs[0][:i]
        return strs[0]