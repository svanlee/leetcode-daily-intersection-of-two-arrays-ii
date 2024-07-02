from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both input lists to enable efficient intersection finding
        nums1.sort()
        nums2.sort()
        
        # Initialize two pointers, one for each list
        i, j = 0, 0
        
        # Initialize an empty list to store the intersection
        intersection = []
        
        # Iterate through both lists until we reach the end of either one
        while i < len(nums1) and j < len(nums2):
            # If the current element in nums1 is smaller, move the pointer forward
            if nums1[i] < nums2[j]:
                i += 1
            # If the current element in nums2 is smaller, move the pointer forward
            elif nums1[i] > nums2[j]:
                j += 1
            # If the current elements are equal, add it to the intersection and move both pointers
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1
        
        # Return the intersection list
        return intersection