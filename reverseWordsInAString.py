def reverseWords(s):
    """
    example: "the sky is blue"
    output: "blue is sky the"
    """

    # loop from back until first space
    # while no space out everything in stack
    # when there is space output stack into new string
    # and continue for next word
    # for letter in range(len(s)-1, 0, -1):
    stack = []
    reversed_string = ""

    i = len(s) - 1
    last = False
    while i >= 0:
        if s[i] == " ":
            while stack:
                reversed_string += stack.pop()
            reversed_string += " "
        else:
            stack.append(s[i])
        i -= 1

    # have to add this line to account for the last word --> how to do it without this line?
    while stack:
        reversed_string += stack.pop()


    reversed_string = " ".join(reversed_string.split())
    # .split splits string into list of strings seperated by space no matter how many spaces, it will split 
    # .join joins the list of string with " "

    return reversed_string


print(reverseWords("a good   example"))