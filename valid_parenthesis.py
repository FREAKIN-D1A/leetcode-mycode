def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack:
                return False
            elif stack.pop() != bracket_map[char]:
                return False
        else:
            return False
    return not stack


"""
def isValid(self, s):
    stack = []  # create an empty stack to store opening brackets
    for c in s:  # loop through each character in the string
        if c in "([{":  # if the character is an opening bracket
            stack.append(c)  # push it onto the stack
        else:  # if the character is a closing bracket
            if (
                not stack
                or (c == ")" and stack[-1] != "(")
                or (c == "}" and stack[-1] != "{")
                or (c == "]" and stack[-1] != "[")
            ):
                return False  # the string is not valid, so return false
            stack.pop()  # otherwise, pop the opening bracket from the stack
    return (
        not stack
    )  # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
    # so the string is valid, otherwise, there are unmatched opening brackets, so return false
"""

# Example usage:
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
