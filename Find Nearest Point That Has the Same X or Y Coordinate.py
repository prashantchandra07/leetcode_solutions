#   Question: https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        l = []
        for i in points:
            print(i,x,y)
            if (i[0]==x or i[1]==y):
                x1 = abs(i[0]-x)
                y1 = abs(i[1]-y)
                md = x1+y1
                l.append(md)
            else:
                l.append(10000000)
                
        print(l)
        if (min(l) == 10000000):
            return(-1)
        else:
            return(l.index(min(l)))