def checkValidParentheses(s: str) -> bool:
    balance = 0 
    
    for char in s:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        

        if balance < 0:
            return False
    

    return balance == 0


s = "(())"

print(checkValidParentheses(s)) 