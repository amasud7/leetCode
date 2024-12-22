def maxArea(height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """

#         # brute force --> O(n^2)
#         max_area = 0
#         for i in range(0, len(height)):
#                 for j in range(i+1, len(height)):
#                         area = (j-i) * min(height[i], height[j])
#                         max_area = max(max_area, area)

        # two pointer solution --> O(n)
        max_area = 0
        index_left = 0
        index_right = len(height) - 1
        while index_left < index_right:
                area = (index_right - index_left) * min(height[index_left], height[index_right])
                max_area = max(max_area, area)
                if height[index_left] < height[index_right]:
                        index_left += 1
                else:
                        index_right -= 1
                
        return max_area


# finding the max
height = [1,8,6,2,5,4,8,3,7]

# brute force is not good
# have one pointer at beginning of array and one at the end --> move only the pointer with the smaller height
# we are trying to find the biggest numbers that are farthest apart from each other

print(maxArea(height)) # 49