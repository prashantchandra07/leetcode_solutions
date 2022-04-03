class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = []
        if len(s) == len(t):
            
            for i in s:
                a = s.count(i)
                b = t.count(i)
                if a == b:
                    l.append(i)
                    
            if len(l) == len(s):
                return(True)
            else:
                return(False)
        else:
            return(False)