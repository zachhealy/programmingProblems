'''
4. Median of Two Sorted Arrays

Difficulty: Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
  
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = []
        total = 0
        
        for i in range(len(nums1)):
            merge.append(nums1[i])
            
        for i in range(len(nums2)):
            merge.append(nums2[i])
            
        merge.sort()
        x = len(merge)
        y = ceil(len(merge)/2)
        
        if x % 2 != 0:
            return merge[y - 1]
        else:
            return (merge[y] + merge[y - 1])/2
        
        return total
