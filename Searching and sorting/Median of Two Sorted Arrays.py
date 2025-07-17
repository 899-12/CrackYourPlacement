
    
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        
        # Calculate the length of the merged array
        total_length = len(merged)
        
        # Check if the length is even or odd
        if total_length % 2 == 0:
            # If even, calculate the average of the middle two elements
            middle_left = merged[total_length // 2 - 1]
            middle_right = merged[total_length // 2]
            median = (middle_left + middle_right) / 2.0
        else:
            # If odd, the median is the middle element
            median = merged[total_length // 2]
        
        return median
