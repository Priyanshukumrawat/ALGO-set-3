def isValid(s: str) -> bool:
    # Dictionary to map closing brackets to corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:  # If the character is a closing bracket
            top_element = stack.pop() if stack else '#'  # Get the top element if stack is not empty, else use a dummy value
            if bracket_map[char] != top_element:  # Check if it matches the corresponding opening bracket
                return False
        else:
            stack.append(char)  # If it's an opening bracket, push it onto the stack
    
    # If the stack is empty, all brackets are matched
    return not stack

# Test cases
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False
print(isValid("([])"))    # Output: True