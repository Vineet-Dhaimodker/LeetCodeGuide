# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
       
        l=1
        r=n
        bvf=False
        # print(isBadVersion(mid)=True)
        while not bvf:
            mid=(l+r)//2
            if isBadVersion(mid)==True:
                if isBadVersion(mid-1)==False:
                    return mid
                else:
                    r=mid-1
            else:
                l=mid+1