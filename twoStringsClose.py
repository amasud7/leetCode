def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # for operation 1 check if the len of the words are different
        if len(word1) != len(word2):
              return False
        
        dict1 = {}
        dict2 = {}

        # create frequency dict for both words
        for char in word1:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1

        for char1 in word2:
            if char1 in dict2:
                dict2[char1] += 1
            else:
                 dict2[char1] = 1
        
        # check if each dict has the same values, then operation 2 is possible
        # two conditions must be true:
        # 1. the set of unique letters must be the same for each word (we use set for this)
        # 2. the frequency of each letter in each word must be the same (use sorted() to check exactly if the same values exist in each dict)

        return set(dict1.keys()) == set(dict2.keys()) and sorted(dict1.values()) == sorted(dict2.values())
        
                





# if word1 and word2 are not the same length, return false bc its impossible to make them the same
# checking operation 1 is checked by the length of each string. if u have same length string with same characters swapping can be done anyway to get the same word
# to check for operation 2, the values(frequency of each letter) in each dict should match up, not each letter but the actual values that are in the dict



