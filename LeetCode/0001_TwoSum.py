class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         # print(i,j)
        #         if nums[i]+nums[j]==target:
        #             # print(nums[i],nums[j])
        #             return [i,j]
        dicti={}
        for i in range(len(nums)):
            if nums[i] in dicti:
                print("1111")
                return [dicti[nums[i]],i]
            else:
                dicti[target-nums[i]]=i