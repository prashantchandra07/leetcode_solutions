class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = nums1
        for i in nums2:
            l.append(i)
            
        l.sort()
        s = int((len(l)+1)/2)
        
        if len(l)%2 == 1:
            ans = format(l[s-1],'.5f')
            return float(ans)
        else:
            k = (l[s-1]+l[s])/2
            ans = format(k,'.5f')
            return float(ans)