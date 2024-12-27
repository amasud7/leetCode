def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        # convert to sets
        set1 = set(nums1)
        set2 = set(nums2)

        # find difference
        answer1 = list(set1 - set2) # numbers that are in set1 but not in set2, also cast them back to lists b/c that is what problem wants
        answer2 = list(set2 - set1) # numbers that are in set2 but not in set1

        return [answer1, answer2]



"""
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
"""
