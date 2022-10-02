#   Question: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = []
        for i in ransomNote:
            if ransomNote.count(str(i)) <= magazine.count(str(i)):
                l.append(i)
                
        if len(l) == len(ransomNote):
            return (True)
        else:
            return(False)
        