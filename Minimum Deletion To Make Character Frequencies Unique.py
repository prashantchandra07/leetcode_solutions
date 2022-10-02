#   Question: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        dct = {}
        m = set(s)
        for i in m:
            k = s.count(i)
            dct[i] = k
            
        visited = set()
        delete = 0
                
        for value in dct.values():
            while value in visited:
                value -= 1
                delete += 1
                
            if value>0:
                visited.add(value)
                
        return delete
