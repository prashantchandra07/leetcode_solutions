#   Question:   https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        
        for i in range(0,a):
            for j in range(1,a):
                if i != j:
                    if nums[i]+nums[j] == target:
                        return(i,j)
                