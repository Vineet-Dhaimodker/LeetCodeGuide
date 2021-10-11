class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        mid=l//2
        # print(mid)
        left = nums[:mid]
        right = nums[mid:]
        
        if l==1:
            return mid if target==nums[mid] else -1
        
        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            return self.search(left,target)
        elif target>nums[mid]:
            return mid+self.search(right,target) if self.search(right,target) is not -1 else -1
            