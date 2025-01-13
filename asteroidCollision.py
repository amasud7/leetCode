class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids: # loop through list
            if asteroid > 0: # when number is pos
                stack.append(asteroid)
            else: # when the number is neg
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)
                else:
                    while stack and asteroid < 0 < stack[-1]: # while there is still smt in stack
                        if stack[-1] > abs(asteroid): # if the top of stack is larger
                            break
                        elif stack[-1] < abs(asteroid): # if the top of stack is smaller
                            stack.pop()
                        else: # when they are equal
                            stack.pop()
                            break
                    else: # this else block is for the while loop, it only runs when the while loop terminates normally, as in it did not hit any break statements
                        stack.append(asteroid)

        return stack


# from stack problem set
# if two asteroids have the same sign they will never meet
# Start from start of array, compare sign if same sign go to next num,
# once sign is different, check which asteroid explodes

# use a stack
# if in positive direction push to stack
# if in negative direction check stack, if empty or also negative, push to stack
# if not compare values and pop whichever is smaller

# empty list is false
# non empty list is true

asteroids = [-2, -2, 1, -2]
stack = []

for asteroid in asteroids:
    if asteroid > 0: # when number is pos
        stack.append(asteroid)
    else: # when the number is neg
        if len(stack) == 0 or stack[-1] < 0:
            stack.append(asteroid)
        else:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] > abs(asteroid):
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else: # when they are equal
                    stack.pop()
                    break
            else: # this else block is for the while loop, it only runs when the while loop terminates normally, as in it did not hit any break statements
                stack.append(asteroid)
        
print(stack) 

