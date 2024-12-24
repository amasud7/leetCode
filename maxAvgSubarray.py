def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # slow solution --> O(n^2)
        # max_avg = 0
        # for i in range(0, len(nums)):
        #         if i+k <= len(nums):
        #                 for j in range(i, i+k):
        #                         avg = sum(nums[i:i+k])/k
        #                         max_avg = max(max_avg, avg)


        # sliding window solution
        window = sum(nums[:k])
        max_avg = window
        for i in range(k, len(nums)):
                window = window - nums[i-k] + nums[i]
                max_avg = max(max_avg, window)
        return max_avg/float(k)


# sliding window solutionn
# start with n length window
# move window to the right
# subtract the left element and add the right element that comes into the window
