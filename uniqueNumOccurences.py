def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dict = {}

        for num in arr:
                if num in dict:
                        dict[num] += 1
                else:
                        dict[num] = 1
        
        return len(set(dict.values())) == len(dict.values())



# create dict
# key will be the number
# value will be the occurence of that number within list
# loop through list and update values as needed

# then check to see if any values in dict are the same, if it is same then return false, if the same value does not exist in dict return true

arr = [-3,0,1,-3,1,1,1,-3,10,0]
dict = {}


# fill in dict with freuqency
for num in arr:
        if num in dict: # if num is already in dict, increase frequency
                dict[num] += 1
        else: # else add num to dict
                dict[num] = 1


# to check if there are values twice in dict

# first create set of values in dict, this will get rid of any duplicates

# now compare the set with the length of values in dict, if they are the same then no duplicates, if they are different then there are duplicates
if len(set(dict.values())) != len(dict.values()):
        print("false") # this means there are duplicates
else:
        print("true")