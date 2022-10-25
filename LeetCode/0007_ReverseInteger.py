class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        m = str(abs(x))
            
        reversed = int(m[::-1])
        
        if reversed > 2147483647:
            return 0

        return reversed if x > 0 else (reversed * -1)