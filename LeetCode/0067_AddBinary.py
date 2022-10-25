class Solution(object):
    def addBinary(self, c, d):
        x,y = int(c,2) , int (d,2)
        return str(bin(x+y).replace("0b",""))