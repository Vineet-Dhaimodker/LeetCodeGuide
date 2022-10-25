from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        for i in list(permutations(nums)):
            l.append(list(i))
        return l
