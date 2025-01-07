class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_merged_array = sorted(nums1+nums2)
        if len(sorted_merged_array)%2==1:
            return sorted_merged_array[len(sorted_merged_array)//2]
        else:
            return float(sorted_merged_array[len(sorted_merged_array)//2] + sorted_merged_array[(len(sorted_merged_array)//2) -1])/2
        