class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        length_of_list = len(nums)
        length_of_set = len(set(nums))
        
        diff = length_of_list - length_of_set
        
        if diff > 0:
            return (True)
        else :
            return (False)