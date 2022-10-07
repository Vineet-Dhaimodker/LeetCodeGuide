class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set(map(str,[p1,p2,p3,p4]))) != 4:
            return False
        distance = lambda p1, p2: round(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5, 2)
        goc_2_vector = lambda p1, p2, p3: (p2[0]-p1[0])*(p3[0] - p1[0]) == -(p2[1]-p1[1])*(p3[1] - p1[1])
        d12 = distance(p1, p2)
        d14 = distance(p1, p4)
        
        if d12 == d14:
            if goc_2_vector(p1,p2,p4):
                if d12 == distance(p2, p3) == distance(p3, p4):
                    return True
        
        d13 = distance(p1, p3)
        
        if d12 == d13:
            if goc_2_vector(p1,p2,p3):
                if d12 == distance(p2, p4) == distance(p3, p4):
                    return True
        
        if d13 == d14:
            if goc_2_vector(p1,p3,p4):
                if d13 == distance(p2, p3) == distance(p2, p4):
                    return True
        
        return False