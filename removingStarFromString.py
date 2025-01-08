def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [] # create stack
        for char in s: # loop through string 
            if char != "*": # if not star, put char into stack
                stack.append(char)
            else: # else pop character from stack
                 stack.pop()
        word = "".join(stack) # join the letters in stack together (this is not using actual stack mechanics)
        return word

# loop through the string
# if current char is not a star then add to stack
# if current char is a star, pop one char from the stack
# continue until string is done
# at the end pop everything from stack and reverse the string to get answer

#ex
# s = "leet**cod*e"
# output = "lecoe"
