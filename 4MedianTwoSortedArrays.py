class Solution:
    @classmethod
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:

        merged = nums1 + nums2
        merged = sorted(merged)

        if len(merged)%2 == 0:
            return (merged[len(merged)//2]+merged[len(merged)//2-1])/2
        
        if len(merged)%2 != 0:
            return merged[len(merged)//2]

# This is too easy if you use python sorted method.
Solution.findMedianSortedArrays([1,2],[3,4])
