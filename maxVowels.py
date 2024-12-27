def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # does not pass all test cases


        # max_vowels = 0
        # vowels = ["a", "e", "i", "o", "u"] # list of vowels
        # window = s[:k] # intial window
        # for i in range(k, len(s)): # iterate through rest of string after initial window
        #         curr_vowels = 0
        #         for c in window: # check how many vowels in current window
        #                 if c in vowels:
        #                         curr_vowels += 1
        #         if curr_vowels == k: # if max number of vowels in window no need to check anymore
        #                 return k
        #         window = window[1:] + s[i] # update window size, remove first element and add next element
        #         max_vowels = max(max_vowels, curr_vowels) # keep max
        # return max_vowels


        # sliding window solution
        max_vowels = 0
        count = 0
        vowels = ['a', 'e', 'u', 'i', 'o']

        # initial window
        window = s[:k]

        # check initial window
        for letter in window:
                if letter in vowels:
                        count += 1

        max_vowels = count

        # loop through rest of windows
        for i in range(k, len(s)):
                window = window[1:] + s[i] # slide window
                if s[i] in vowels: # if the letter thats coming into window is vowel plus 1
                        count += 1
                if s[i-k] in vowels: # if the letter that left window is vowel minus 1
                        count -= 1

                if count == k: # if we reach k vowels return k because that is the max, no need to check other windows 
                        return k
                
                max_vowels = max(max_vowels, count) # update which window has the max number of vowels

        return max_vowels


# use sliding window method to find
# if the current window has the max number of vowels (k) then return that b/c no reason to check further

# if the letter that is leaving window. subtract one
# if the letter that is entering window is a vowel add one
