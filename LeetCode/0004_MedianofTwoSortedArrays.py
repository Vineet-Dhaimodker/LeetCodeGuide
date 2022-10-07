class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_list = sorted(nums1 + nums2)
        return (merge_list[(len(merge_list)-1) // 2] + merge_list[(len(merge_list)) // 2]) / 2