class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxA=(j-i)*min(height[i],height[j])
        while(j-i>0):
            if height[i]>height[j]:
                j-=1
                maxA=max(maxA,(j-i)*min(height[i],height[j]))
            else:
                i+=1
                maxA=max(maxA,(j-i)*min(height[i],height[j]))
        return maxA