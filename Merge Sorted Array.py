#   Question: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = n
        while k > 0:
            nums1.pop()
            k = k-1
            
        for i in nums2:
            nums1.append(i)
            
        nums1.sort()
            
        return (nums1)
  